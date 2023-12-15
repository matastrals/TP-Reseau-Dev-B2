import asyncio
import websockets

global CLIENTS
CLIENTS = {}

async def handle_packet(websockets):
    while True:
        try:
            data = await websockets.recv()
            addr = websockets.remote_address
        except:
            message = "Annonce : " + CLIENTS[addr]["pseudo"] + " a quitté le chatroom"
            for client in CLIENTS:
                if client == addr:
                    continue
                try:
                    await CLIENTS[client]["w"].send(message.encode())
                except Exception as e:
                    print(e)
            del CLIENTS[addr]
            break
            
        else:
            message = data.decode()
        new_user = False

        if message[0:5] == "Hello" and not addr in CLIENTS:
            CLIENTS[addr] = {}
            CLIENTS[addr]["pseudo"] = message[6:]
            CLIENTS[addr]["w"] = websockets
            new_user = True

        print("Message received from", CLIENTS[addr]["pseudo"], ":", message)

        # Si l'utilisateur est nouveau, on fait une annonce
        if new_user == True:
            message = "Annonce : " + CLIENTS[addr]["pseudo"] + " a rejoint le chatroom"
        else:
            message = CLIENTS[addr]["pseudo"] + " a dit : " + message

        for client in CLIENTS:
            if client == addr:
                continue
            try:
                await CLIENTS[client]["w"].send(message.encode())
            except Exception as e:
                print(e)



async def main():   
    server = await websockets.serve(handle_packet, "127.0.0.1", 13337)
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await asyncio.Future() 



if __name__ == "__main__":
    asyncio.run(main())