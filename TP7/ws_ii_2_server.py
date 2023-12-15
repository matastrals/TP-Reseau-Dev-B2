import asyncio
import websockets
import redis.asyncio as redis

global CLIENTS
CLIENTS = {}

async def handle_packet(websockets):
    while True:
        try:
            data = await websockets.recv()
            addr = websockets.remote_address
        except:
            client_pseudo = await get_data_base(addr[0], addr[1], "pseudo")
            message = "Annonce : " + client_pseudo.decode() + " a quitté le chatroom"
            for client in CLIENTS:
                if client == addr:
                    continue
                try:
                    await CLIENTS[client]["w"].send(message.encode())
                except Exception as e:
                    print(e)
            del CLIENTS[addr]
            break
        
        message = data.decode()
        new_user = False
        

        if message[0:5] == "Hello" and not addr in CLIENTS:
            CLIENTS[addr] = {}
            await set_data_base(addr[0], addr[1], "pseudo", value = message[6:]) 
            CLIENTS[addr]["w"] = websockets
            new_user = True
            
        client_pseudo = await get_data_base(addr[0], addr[1], "pseudo")
        print("Message received from", client_pseudo.decode(), ":", message)

        # Si l'utilisateur est nouveau, on fait une annonce
        if new_user == True:
            client_pseudo = await get_data_base(addr[0], addr[1], "pseudo")
            message = "Annonce : " + client_pseudo.decode() + " a rejoint le chatroom"
        else:
            client_pseudo = await get_data_base(addr[0], addr[1], "pseudo")
            message = client_pseudo.decode() + " a dit : " + message

        for client in CLIENTS:
            if client == addr:
                continue
            try:
                await CLIENTS[client]["w"].send(message.encode())
            except Exception as e:
                print(e)


async def set_data_base(ip, port, key, value):

    addr = ip + ":" + str(port)
    client = await redis.Redis(host="10.33.76.235", port=6379)
    await client.set(addr + key, value)

async def get_data_base(ip, port, key):
    addr = ip + ":" + str(port)
    client = await redis.Redis(host="10.33.76.235", port=6379)
    return await client.get(addr + key)



async def main():   
    server = await websockets.serve(handle_packet, "127.0.0.1", 13337)
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await asyncio.Future() 



if __name__ == "__main__":
    asyncio.run(main())