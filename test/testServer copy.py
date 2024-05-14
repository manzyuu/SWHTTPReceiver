from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import datetime
import threading

#オーバーライド
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        dt_now = datetime.datetime.now()
  
        print("get\n")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        text=str(dt_now)
        self.wfile.write(text.encode())


#鯖実行
def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
#run()

run()