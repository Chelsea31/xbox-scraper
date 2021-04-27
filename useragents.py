# A util to gather easily available header list

import requests
from bs4 import BeautifulSoup

url = "https://developers.whatismybrowser.com/useragents/explore/software_name/opera/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}


def getSoup(url):
    r = requests.get(url, headers=headers)
    return BeautifulSoup(r.content, "html.parser")


soup = getSoup(url)
user_agents = list(soup.findAll("a", class_="useragent"))

with open("user_agents.txt", "a") as file:
    for agent in user_agents:
        file.write(agent.next_element + "\n")


with open("user_agents.txt", "r") as read_file:
    line = read_file.readline()
    while line:
        print (line)
        line = read_file.readline()