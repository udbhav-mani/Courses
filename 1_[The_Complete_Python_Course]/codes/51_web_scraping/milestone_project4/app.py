import requests
from pages.all_books_page import ALlBooksPage

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list.')

book_objects = []
for i in range(1, 51):
    page_content = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html").content
    pages = ALlBooksPage(page_content)
    book_objectlist = pages.books
    # print(book_objectlist)
    book_objects.extend((book_objectlist))