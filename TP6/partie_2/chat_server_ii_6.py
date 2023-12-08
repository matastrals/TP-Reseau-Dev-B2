import asyncio

global CLIENTS
CLIENTS = {}

async def handle_packet(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            message = "Annonce : " + CLIENTS[addr]["pseudo"] + " a quitté le chatroom"
            for client in CLIENTS:
                if client == addr:
                    continue
                try:
                    CLIENTS[client]["w"].write(message.encode())
                    await CLIENTS[client]["w"].drain()
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
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer
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
                CLIENTS[client]["w"].write(message.encode())
                await CLIENTS[client]["w"].drain()
            except Exception as e:
                print(e)



async def main():
    server = await asyncio.start_server(handle_packet, "127.0.0.1", 13337)
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())