import asyncio
import aiohttp
import time


async def fetch_page(url):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"This page took {time.time() - start} seconds.")
            return response.status


# loop = asyncio.get_event_loop()
# loop.run_until_complete(fetch_page("https://google.com"))


loop = asyncio.get_event_loop()
tasks = [fetch_page("https://books.toscrape.com/") for i in range(50)]
start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))
print(f"All pages took {time.time() - start} seconds.")
