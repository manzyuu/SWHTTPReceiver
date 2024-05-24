import websockets
from websockets.exceptions import InvalidURI, InvalidHandshake, ConnectionClosedError, WebSocketException

class WebSocketClient:
    def __init__(self, url: str):
        self.url = url
        self.websocket = None

    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.url)
            print(f"Connected to {self.url}")
            return ""
        except InvalidURI:
            print(f"Error: The URL '{self.url}' is invalid.")
        except InvalidHandshake:
            print(f"Error: Handshake failed for URL '{self.url}'.")
        except ConnectionClosedError:
            print(f"Error: Connection to '{self.url}' was closed unexpectedly.")
        except WebSocketException as e:
            print(f"WebSocket error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return None 

    async def send_and_receive(self, message: str) -> str:
        if self.websocket is None:
            print("Error: WebSocket is not connected.")
            return ""

        try:
            #print(f"Sending message: {message}")
            await self.websocket.send(message)
            
            response = await self.websocket.recv()
            #print(f"Received response: {response}")
            return str(response)
        except ConnectionClosedError:
            print(f"Error: Connection to '{self.url}' was closed unexpectedly.")
            return ""
        except WebSocketException as e:
            print(f"WebSocket error occurred: {e}")
            return ""
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return ""

    async def close(self):
        if self.websocket is not None:
            await self.websocket.close()
            print(f"Connection to {self.url} closed.")
