from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE

        return [
            QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, locator)
        ]

    @property
    def author_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.AUTHOR_DROPDOWN
        )

        return Select(element)

    def select_author(self, author_name):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tags_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.TAG_DROPDOWN
        )

        return Select(element)

    def get_available_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name):
        self.tags_dropdown.select_by_visible_text(tag_name)

    @property
    def search_button(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, QuotesPageLocators.SEARCH_DROPDOWN
        )

    def search_quote(self, author, tag):
        self.select_author(author)
        self.select_tag(tag)
        self.search_button.click()
        return self.quotes
