import asyncio
import websockets

async def hello(websocket):
    data = await websocket.recv()
    print(f"<<< {data}")
    greeting = f"Hello client ! Received {data}!"
    await websocket.send(greeting)
    print(f">>> {greeting}")


async def main():
    async with websockets.serve(hello, "127.0.0.1", 13543):
        await asyncio.Future()  # run forever
    
if __name__ == "__main__":
    asyncio.run(main())
