import requests
from bs4 import BeautifulSoup
from check_price import CheckPrice
from send_alert import SendAlert


product_url = "https://www.amazon.in/Alchemist-Paulo-Coelho/dp/8172234988/ref=sr_1_3?keywords=the+alchemist&sr=8-3"
alert_price = 300

check_price = CheckPrice(product_url)

current_price = check_price.current_price()

print(current_price)


if current_price is not None and current_price <= int(alert_price):
    send_alert = SendAlert(product_url, current_price)

else:
    print("Error")