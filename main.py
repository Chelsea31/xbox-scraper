import random

import requests
from bs4 import BeautifulSoup

amazon_urls = ["https://www.amazon.in/Xbox-Series-X/dp/B08J7QX1N1"]
flipkart_urls = ["https://www.flipkart.com/microsoft-xbox-series-x-1024-gb/p/itm63ff9bd504f27"]
reliance_url = ["https://www.reliancedigital.in/xbox-series-x-console-with-wireless-controller-1-tb/p/491934660"]
user_agent_list = []


def create_header_list():
    with open("user_agents.txt", "r") as read_file:
        line = read_file.readline()
        while line:
            line = line.replace("\n", "")
            user_agent_list.append(line)
            line = read_file.readline()


def get_random_user_agent():
    return random.choice(user_agent_list)


def getSoup(url):
    r = requests.get(url, headers={"user_agent": get_random_user_agent()})
    return BeautifulSoup(r.content, "html.parser")


def check_amazon(url):
    soup = getSoup(url)
    div_data = list(soup.find_all("input", id="add-to-cart-button"))
    if div_data:
        print("Found stock on amazon: " + url)
        return True
    else:
        return False


def check_flipkart(url):
    soup = getSoup(url)
    button_data = list(soup.find_all("button", class_="_2KpZ6l _2U9uOA ihZ75k _3AWRsL"))
    if button_data:
        print("Found stock on flipkart: " + url)
        return True
    else:
        return False


def check_reliance(url):
    soup = getSoup(url)
    button_list = list(soup.find_all("button", id="add_to_cart_main_btn"))
    if button_list:
        print("Found stock on RD : " + url)
        return True
    else:
        return False


if __name__ == '__main__':
    create_header_list()
    result_rd = [check_reliance(url) for url in reliance_url]
    result_amazon = [check_amazon(url) for url in amazon_urls]
    result_flipkart = [check_flipkart(url) for url in flipkart_urls]
    print("The end..")
