import asyncio
import aiohttp
import aiofiles
import sys
import time

async def get_content(url:str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            return response
    

async def write_content(content, file):
    async with aiofiles.open("tmp/" + str(file), "w") as out:
        await out.write(str(content))
        await out.flush() 


async def read_file():
    async with aiofiles.open("tmp/contains_url.txt") as out:
        line = []
        for _ in range(10):
            line.append(await out.readline())
        return line
        


async def main():
    tab_url = await read_file()
    tasks = [write_content(await get_content(tab_url[i][:-1]), tab_url[i][8:-2]) for i in range (10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        start = time.perf_counter ()
        asyncio.run(main())
        stop = time.perf_counter()
        print("Done in {} seconds".format(stop - start))
        print()
    elif (len(sys.argv)) < 2:
        print("Missing argument")
    elif (len(sys.argv)) > 2:
        print("Too much argument")
    