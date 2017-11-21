# https://gist.github.com/dergachev/7028596
import BaseHTTPServer, SimpleHTTPServer

IP='192.168.0.25'
PORT=4444
LOCATION=("http://%(ip)s:%(port)d/usermedia.html" % {'ip': IP, 'port': PORT})

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/redirect.html':
      self.send_response(301)
      self.send_header('Location', LOCATION)
      self.end_headers()
    else:
      return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = BaseHTTPServer.HTTPServer((IP, PORT), myHandler)
httpd.serve_forever()
