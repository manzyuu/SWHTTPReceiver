import datetime
import asyncio
import threading
import time
#handmade
from socketClient import WebSocketClient
from JsonControl import JsonControl
import HTTPServer 
import calculation


    
    
def main():
    #Configあったら次へ。なければ作る
    config=JsonControl("config.json")
    if config.check() is None:
        print("!!!Configfile is not find")
        config.data["Websoket"]["URL"]=input("Please inout Server Address\n")
        config.write()

    config.load()
    #url = "ws://localhost:8765"

    client = WebSocketClient(config.data["Websoket"]["URL"])

    
    
    
    async def run_client():
        while True:#アドレス開通まで周回
            if await client.connect() is None:
                config.data["Websoket"]["URL"]=input("Please inout Server Address\n")
                config.write()
                client.url=config.data["Websoket"]["URL"]
            else:break

        while True:
            calculation.data["time"] = await client.send_and_receive( str(datetime.datetime.now()))
            #print(f"Response 1: {calculation.data['time']}")
            time.sleep(0.01)
        
        #await client.close()
    #asyncio.run(run_client())
    HTTPThread = threading.Thread(target=HTTPServer.HTTPrun, daemon=True)
    HTTPThread.start()

    
    # WebSocketクライアントをイベントループ内で実行
    loop = asyncio.get_event_loop()
    loop.create_task(run_client())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
    

    

if __name__ == "__main__":
    #HTTPServer.HTTPrun()
    main()
    
    

    