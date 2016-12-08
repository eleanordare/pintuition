#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

from bottle import Bottle, get, post, request, put, delete, run, route, ServerAdapter, static_file, template
import json
import BaseHTTPServer, SimpleHTTPServer
import ssl
from data_to_highcharts import HighchartsMethods

access_token="AWRuspwOpmEWxbbkTD2gGNDnmt79FIzt04E4NzVDmoq4pAAu4AAAAAA"

# content on page
@route('/hello')
def addPage():
    highchartsMethods = HighchartsMethods()
    highchartsMethods.main()
    return template('Chart.html')


# # adding a new server
# @post('/hello')
# def add():
#
#
# # changing an existing server
# @put('/hello')
# def update():
#
#
# # delete an existing server
# @delete('/hello')
# def delete():
#



class SSLWSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        import ssl
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        srv = make_server(self.host, self.port, handler, **self.options)
        srv.socket = ssl.wrap_socket (
         srv.socket,
         certfile='server.crt',  # path to certificate
         keyfile='server.key',
         server_side=True)
        srv.serve_forever()

srv = SSLWSGIRefServer(host="127.0.0.1", port=5000)
run(server=srv)

# run(host='localhost', port=5000)
