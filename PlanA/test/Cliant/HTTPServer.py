from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import datetime
import calculation

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # クエリパラメータを解析
        parsed_path = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_path.query)

        # 取得したクエリパラメータをログに出力
        print("Query Params:", query_params)

        # 実験的返答(RialTime)
        dt_now = str(datetime.datetime.now())
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(dt_now.encode())

def HTTPrun(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    print("HTTPServer is Active")
    server_address = ('localhost', 8080)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping HTTPServer")

if __name__ == "__main__":
    print("testRun")
    HTTPrun()