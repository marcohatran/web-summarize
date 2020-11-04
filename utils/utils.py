# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import urlparse
import nltk
from gensim.summarization import summarize as g_sumn
from ftfy import fix_text
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
    content = []
    for param in params:
        txt = fix_text(param.text)
        content.append(txt)
    

    content = ' '.join(content)

    return content
def get_title_from(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,"lxml")
    param = soup.find("h1")
    return param.text

def get_domain(url):
    res = urlparse(url)[1]
    return res

def gen_summary(text):
    sent = nltk.sent_tokenize(text)
    if len(sent) < 2:
        summary1 =  "please pass more than 3 sentences to summarize the text"
    else:
        summary = g_sumn(text)
        summ = nltk.sent_tokenize(summary)
        summary1 = (" ".join(summ[:2]))
    return summary1

