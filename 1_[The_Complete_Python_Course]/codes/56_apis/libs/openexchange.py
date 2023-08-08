import requests


class OpenExchangeLibrary:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, appid) -> None:
        self.appid = appid

    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.appid}").json()

    def convert(self, amount, from_currency, to_currency):
        rates = self.latest["rates"]
        if from_currency == "USD":
            print(
                f"{amount} {from_currency} is {amount*self.rates[to_currency]} {to_currency}."
            )
        else:
            rates = self.latest["rates"]
            in_usd = amount / (rates)[from_currency]
            converted = in_usd * (rates)[to_currency]
            # print(converted)
            print(f"{amount} {from_currency} is {converted} {to_currency}.")
