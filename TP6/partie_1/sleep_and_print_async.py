import asyncio
import time

async def compte_to_ten():
    for i in range(11):
        print(i)
        await asyncio.sleep(0.5)
   
    


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        loop.create_task(compte_to_ten()),
        loop.create_task(compte_to_ten())
    ]
    start = time.perf_counter()
    loop.run_until_complete(asyncio.wait(tasks))
    stop = time.perf_counter()
    print("Done in {} seconds".format(stop - start))
    loop.close()
