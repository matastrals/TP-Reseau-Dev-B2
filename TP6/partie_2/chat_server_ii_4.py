import asyncio

global CLIENTS
CLIENTS = {}

async def handle_packet(reader, writer):
    while True:
        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')
        if data == b'':
            break

        message = data.decode()

        if not addr in CLIENTS:
            CLIENTS[addr] = {}
            CLIENTS[addr]["r"] = reader
            CLIENTS[addr]["w"] = writer

        try:
            message = f"{addr[0]}:{addr[1]} a dit : " + message
        except Exception as e:
            print("L'erreurrrr", e)

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