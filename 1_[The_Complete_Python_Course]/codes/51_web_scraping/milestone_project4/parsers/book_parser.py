import re

from locators.book_locators import BookLocators


class BookParser:
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,

    }

    def __init__(self, page) -> None:
        self.parent = page

    def __repr__(self):
        return f"{self.get_name} , {self.get_price}, {self.get_rating}."

    @property
    def get_name(self):
        locator = self.parent.select_one(BookLocators.NAME_LOCATOR)
        book_name = locator.attrs["title"]
        return book_name

    @property
    def get_address(self):
        link_address = self.parent.select_one(BookLocators.LINK_LOCATOR).attrs["href"]
        return link_address

    @property
    def get_price(self):
        price = self.parent.select_one(BookLocators.PRICE_LOCATOR).string
        reg = "£([0-9]+\.[0-9]+)"
        matches = re.search(reg, price)
        return float(matches.group(1))

    @property
    def get_rating(self):
        locators = self.parent.select_one(BookLocators.RATING_LOCATOR)
        link_class = locators.attrs['class']
        rating_classes = [r for r in link_class if r != "star-rating"]
        ratings = BookParser.ratings.get(rating_classes[0])
        return ratings
