from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

<<<<<<< HEAD
#鯖実行
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    
#オーバーライド
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write('GETメソッドを実装'.encode())
=======

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
>>>>>>> 16bb2e74be451fbdc79d3910d6d79e986466a5f0
