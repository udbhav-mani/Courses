from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"{self.content} written by {self.author}."

    @property
    def content(self):
        locators = QuoteLocators.CONTENT
        return self.parent.select_one(locators).string

    @property
    def author(self):
        locators = QuoteLocators.AUTHOR
        return self.parent.select_one(locators).string

    @property
    def tags(self):
        locators = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locators)]
