from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import datetime
import threading
import asyncio
import websockets
import requests

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
        
        #html_context = '<html lang="ja">' \
        #               '<meta http-equiv=”refresh” content=”0;URL=http://manzyuu-server.duckdns.org:8000/”>' \
        #               '</html>'
        #self.wfile.write(html_context.encode())
        
        
        #load_url = "http://www.nict.go.jp/JST/JST5.html"
        #
        #html = requests.get(load_url)
        #soup = BeautifulSoup(html.content, "html.parser")
        #self.wfile.write(soup.encode())

#鯖実行
def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
#run()



async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print(await websocket.recv())


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)


def get_gip_addr():
    res = requests.get('https://ifconfig.me')
    return res.text

async def main():
    while True:
        ServerAddr=input("Please input ServerAddr")
        try:
            websockets.connect(ServerAddr)
            break
        except:
            pass
        
    async with websockets.connect(ServerAddr) as websocket:
        await websocket.send(get_gip_addr)
         
    
    thread1 = threading.Thread(target=run)
    thread2 = threading.Thread(target=run)
    thread1.start()
    thread2.start()