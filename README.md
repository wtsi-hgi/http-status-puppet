[![Build Status](https://travis-ci.org/wtsi-hgi/http-status-puppet.svg?branch=master)](https://travis-ci.org/wtsi-hgi/http-status-puppet)
[![codecov](https://codecov.io/gh/wtsi-hgi/http-status-puppet/branch/master/graph/badge.svg)](https://codecov.io/gh/wtsi-hgi/http-status-puppet)
[![PyPI version](https://badge.fury.io/py/httpstatuspuppet.svg)](https://badge.fury.io/py/httpstatuspuppet)

# HTTP Status Puppet
_A HTTP server that will return a status code of your choice_ 


## Introduction
This server simply returns back a status code depending on what endpoint is contacted, e.g.
```
$ curl -s -o /dev/null -w "%{http_code}" http://0.0.0.0:8000/403
403
$ curl -s -o /dev/null -w "%{http_code}" http://0.0.0.0:8000/200
200
```


## Installation
Prerequisites
- Python 3.6+

The tool can be installed from PyPi:
```bash
pip install httpstatuspuppet
```

Bleeding edge versions can be installed directly from GitHub:
```bash
pip install git+https://github.com/wtsi-hgi/http-status-puppet/.git@master#egg=httpstatuspuppet
```


## Usage
_Warning: this server was only designed for use in testing!_

### Local
After installing dependencies, in the project directory:
```bash
PYTHONPATH=. python httpstatuspuppet/entrypoint.py
```

### Docker
```bash
docker run -d -p ${HOST_PORT}:8000 mercury/http-status-puppet
```


## Alternatives
- C# server: https://github.com/Readify/httpstatus.
