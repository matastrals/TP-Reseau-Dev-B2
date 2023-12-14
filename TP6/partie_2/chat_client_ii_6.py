import asyncio
import aioconsole

class StopProgram(Exception):
    pass

async def main(pseudo):
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=13337)
    tasks = [recv_mes(reader), send_mes(writer, pseudo)]
    try:
        await asyncio.gather(*tasks)
    except StopProgram:
        print("Le programme a été arrêté.")

async def recv_mes(reader) -> bool:
    try:
        while True:
            data = await reader.read(1024)
            if data == b"":
                raise StopProgram("Le serveur c'est déconnecté")
            print(data.decode())
    except StopProgram as e:
        print(e)
        raise

async def send_mes(writer, pseudo = ""):
    while True:
        if pseudo == "":
            msg = await aioconsole.ainput()
        else:
            msg = f"Hello|{pseudo}"
            pseudo = ""

        writer.write(msg.encode())
        await writer.drain() 


if __name__ == "__main__":
    pseudo = input("Sous quel pseudo veux tu apparaitre : ")
    asyncio.run(main(pseudo))

