from selenium import webdriver
from selenium.webdriver.common.by import By


from pages.quotes_page import QuotesPage

author = input("Enter author - ")
tag = input("Enter tag - ")

chrome = webdriver.Chrome()
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)


print(page.search_quote(author, tag))
