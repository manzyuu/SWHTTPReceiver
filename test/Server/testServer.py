import asyncio
import websockets
import datetime


async def echo(websocket):
    client_ip = websocket.remote_address[0]
    client_port = websocket.remote_address[1]
    print(f"New connection from IPaddr={client_ip}   Port={client_port}")
    try:
        async for message in websocket:
            print(f" {str(datetime.datetime.now())}\n Received message from {client_ip}:{client_port}: {message}")
            await websocket.send(f"Echo from server: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {client_ip}:{client_port}")

async def main():
    address="ws://manzyuu-server.duckdns.org"
    port=7777
    async with websockets.serve(echo, "localhost", port):
        print("Server started at "+address+":"+str(port))
        await asyncio.Future()  # サーバーを実行し続けるためのブロック

if __name__ == "__main__":
    asyncio.run(main())