from locators.quote_locators import QuoteLocators
from selenium.webdriver.common.by import By


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.content} written by {self.author}."

    @property
    def content(self):
        locators = QuoteLocators.CONTENT_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locators).text

    @property
    def author(self):
        locators = QuoteLocators.AUTHOR_LOCATOR
        return self.parent.find_element(By.CSS_SELECTOR, locators).text

    @property
    def tags(self):
        locators = QuoteLocators.TAGS_LOCATOR
        return [e.string for e in self.parent.find_elements(By.CSS_SELECTOR, locators)]
