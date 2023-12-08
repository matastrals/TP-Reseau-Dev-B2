import asyncio


async def main():
    server = await asyncio.start_server(handle_packet, "127.0.0.1", 13337)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()



async def handle_packet(reader, writer):
    while True:

        data = await reader.read(1024)
        addr = writer.get_extra_info('peername')

        if data == b'':
            break

        message = data.decode()
        print(f"Message received from {addr[0]}:{addr[0]} : {message!r}")

        await writer.drain()


if __name__ == "__main__":
    asyncio.run(main())