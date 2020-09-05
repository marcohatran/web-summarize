from bs4 import BeautifulSoup
import requests
import re

def get_link(link):
    page = requests.get(link).text
    soup = BeautifulSoup(page,"html.parser")
    feeds = soup.find_all("a")
    urls = []
    for feed in feeds:
        url = feed.get('href')
        urls.append(url)
    return urls
def get_data_from_url(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    params =soup.find_all("p")
    print("ok")

    content = []
    for param in params:
        content.append(param.text)

    content = ' '.join(content)

    return content