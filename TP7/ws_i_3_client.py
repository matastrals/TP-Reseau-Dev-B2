import asyncio
import aioconsole
import websockets

class StopProgram(Exception):
    pass

async def main(pseudo):
    url="ws://127.0.0.1:13337"
    ws = await websockets.connect(url)
    tasks = [recv_mes(ws), send_mes(ws, pseudo)]
    try:    
        await asyncio.gather(*tasks)
    except StopProgram:
        print("Le programme a été arrêté.")

async def recv_mes(ws) -> bool:
    try:
        while True:
            data = await ws.recv()
            if data == b"":
                raise StopProgram("Le serveur c'est déconnecté")
            print(data.decode())
    except StopProgram as e:
        print(e)
        raise

async def send_mes(ws, pseudo = ""):
    while True:
        if pseudo == "":
            msg = await aioconsole.ainput()
        else:
            msg = f"Hello|{pseudo}"
            pseudo = ""
        data = msg.encode()
        await ws.send(data)


if __name__ == "__main__":
    pseudo = input("Sous quel pseudo veux tu apparaitre : ")
    asyncio.run(main(pseudo))

