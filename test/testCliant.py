from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import datetime
import requests
import asyncio
import websockets
import threading

count=0

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print(await websocket.recv())


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
    

#オーバーライド
class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global soup
        dt_now = datetime.datetime.now()
        global count
        count=count+1
        print("get\n")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        
        
        
        self.wfile.write(dt_now.encode())

#鯖実行
def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('localhost', 7000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()