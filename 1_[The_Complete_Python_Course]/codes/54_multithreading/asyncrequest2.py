import asyncio
import aiohttp
import time


async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f"This page took {time.time() - start} seconds.")
        return response.status


async def get_all_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()
urls = ["https://books.toscrape.com/" for i in range(50)]
start = time.time()
loop.run_until_complete(get_all_pages(loop, *urls))
print(f"All pages took {time.time() - start} seconds.")
