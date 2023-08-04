import asyncio
import aiohttp
import time
from pages.all_books_page import ALlBooksPage

import logging

loop = asyncio.get_event_loop()


logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename="logs.txt",
)

logger = logging.getLogger("scraping")
logger.info("Loading books list.")


async def fetch_page(session, url):
    start = time.time()
    async with session.get(url) as response:
        print(f"This page took {time.time() - start} seconds.")
        return await response.text()


async def get_all_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


urls = [f"https://books.toscrape.com/catalogue/page-{i}.html" for i in range(1, 51)]
start = time.time()
pages = loop.run_until_complete(get_all_pages(loop, *urls))
print(f"All pages took {time.time() - start} seconds.")

books_object = []
for page_content in pages:
    page = ALlBooksPage(page_content)
    books_object.extend(page.books)
