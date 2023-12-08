import asyncio
import aiohttp
import aiofiles
import sys

async def get_content(url:str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            return response


async def write_content(content, file):
    async with aiofiles.open("tmp/" + file, "w") as out:
        await out.write(str(content))
        await out.flush() 

async def main():
    if (len(sys.argv) == 2): 
        await write_content(await get_content(sys.argv[1]), "test.txt")
    elif (len(sys.argv)) < 2:
        print("Missing argument")
    elif (len(sys.argv)) > 2:
        print("Too much argument")

if __name__ == '__main__':
    asyncio.run(main())
    
