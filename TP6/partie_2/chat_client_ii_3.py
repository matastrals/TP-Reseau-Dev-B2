import asyncio
import aioconsole

async def main():
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=13337)
    tasks = [recv_mes(reader), send_mes(writer)]
    await asyncio.gather(*tasks)
 

async def recv_mes(reader):
    while True:
        data = await reader.read(1024)
        print(data.decode())


async def send_mes(writer):
    while True:
        msg = await aioconsole.ainput()
        writer.write(msg.encode())
        await writer.drain()

if __name__ == "__main__":
    asyncio.run(main())