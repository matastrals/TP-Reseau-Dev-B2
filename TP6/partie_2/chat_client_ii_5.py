import asyncio
import aioconsole

async def main(pseudo):
    reader, writer = await asyncio.open_connection(host="127.0.0.1", port=13337)
    tasks = [recv_mes(reader), send_mes(writer, pseudo)]
    await asyncio.gather(*tasks)
 

async def recv_mes(reader):
    while True:
        data = await reader.read(1024)
        print(data.decode())


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