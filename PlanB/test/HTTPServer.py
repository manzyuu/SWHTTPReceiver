from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse
import datetime
import calculation

dataBase={}

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass# ログ出力を行わない為のオーバーライド
        
    
    
    def do_GET(self):
        template_params={"ver":"",
                         "name":"",
                         "gps_x":"",
                         "gps_y":"",
                         "gps_z":"",
                         "vector":"",
                         "reflectance":"",
                         "":"",
                         "":""
                        }
        #template_URL= http://localhost:8080/?var=0.1&name=戦闘機名&gps_x=0&gps_y=0&gps_z=0&vector=0&reflectance=1.0
        # クエリパラメータを解析
        parsed_path = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_path.query)
        if query_params=={}:#パラメータなしの保護
            dt_now = str(datetime.datetime.now())
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(dt_now.encode())
            return

        # 取得したクエリパラメータをログに出力
        print("Query Params:", query_params)

        # 実験的返答(RialTime)
        text = str("x,y,z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z")
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(text.encode())

def HTTPrun(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    print("HTTPServer is Active")
    server_address = ("localhost", 8080)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping HTTPServer")

if __name__ == "__main__":
    print("testRun")
    HTTPrun()