import requests
from bs4 import BeautifulSoup


class CheckPrice:
    def __init__(self, url) -> None:
        self.product = url

    def current_price(self):
        response = requests.get(self.product)

        webpage = response.text

        soup = BeautifulSoup(webpage, "html.parser")

        price = int(soup.find(name="span", id="price").string.split(
            "₹")[1].split(".")[0])

        return price