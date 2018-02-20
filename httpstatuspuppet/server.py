from threading import Thread
from wsgiref.simple_server import make_server

from http_status import Status

from httpstatuspuppet.common import HttpStatusPuppetError

DEFAULT_HTTP_STATUS = 200
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 8010


class ServerNotStartedError(HttpStatusPuppetError):
    """
    Server not started error.
    """


class InvalidStatusCodeError(HttpStatusPuppetError):
    """
    Invalid status code error.
    """


def _code_and_description(status: Status) -> str:
    """
    Generates "{code} {description}" string from the given status.
    :param status: status to generate code and description string from
    :return: generated string
    """
    return f"{status.code} {status.description}"


class Server:
    """
    Basic authentication server.
    """
    @staticmethod
    def _endpoint(environment, start_response):
        path = environment["PATH_INFO"][1:]
        try:
            raw_status = int(path)
        except ValueError:
            start_response(_code_and_description(Status(400)), [])
            return [f"Unknown status code: {path}".encode("utf-8")]

        status_information = Status(raw_status)
        code_and_description = _code_and_description(status_information)
        start_response(code_and_description, [])
        return [f"{code_and_description}".encode("utf-8")]

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

    def __init__(self, host: str=DEFAULT_HOST, port: int=DEFAULT_PORT):
        """
        Constructor.
        :param host: where to bind server to
        :param port: port to run server on
        """
        self.status_code = DEFAULT_HTTP_STATUS
        self.host = host
        self.port = port
        self._app = Server._endpoint
        self._server = make_server(self.host, self.port, self._app)
        self._running = False

    def start(self):
        """
        Starts the server (non-blocking).
        """
        if not self._running:
            Thread(target=self.run).start()

    def run(self):
        """
        Runs the server (blocking).
        """
        if not self._running:
            self._running = True
            self._server.serve_forever()

    def stop(self):
        """
        Stops the server if running.
        """
        if self._running:
            self._running = False
            self._server.shutdown()
