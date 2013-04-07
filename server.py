#!/usr/bin/env python2

from wsgiref.simple_server import make_server

_port = 8080

def error_401(environ, start_response):
    response = 'Error 401. Unauthorized.'
    status = '401 Unauthorized'
    response_headers = [ ('Content-Type', 'text/plain') ]
    start_response(status, response_headers)
    return [response]

def error_404(environ, start_response):
    response = "File not found."
    status = '404 Not Found'
    response_headers = [ ('Content-Type', 'text/plain') ]
    start_response(status, response_headers)
    return [response]

def get_type(filename):
    if filename.endswith('js'):
        return 'text/javascript'
    if filename.endswith('css'):
        return 'text/css'
    if filename.endswith('html'):
        return 'text/html'

def application(environ, start_response):
    response = ''

    _filename = environ['PATH_INFO'][1:]
    if not _filename:
        _filename = 'index.html'

    if '..' in _filename or _filename.startswith('..'):
        return error_401(environ, start_response)
    
    try:
        with open(_filename) as f:
            response = f.read()
    except IOError:
        return error_404(environ, start_response)

    status = '200 OK'

    response_headers = [ ('Content-Type', get_type(_filename)),
                         ('Content-Length', str(len(response))) ]

    start_response(status, response_headers)

    return [response]

def get_environ(environ, start_response):
    response = [ x + '=' + str(y) + "\n" for x,y in environ.iteritems() ]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return response

if __name__ == '__main__':
    httpd = make_server('localhost', _port, application)
    #httpd = make_server('localhost', _port, get_environ)

    httpd.serve_forever()


