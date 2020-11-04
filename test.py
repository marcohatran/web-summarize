# -*- coding: utf-8 -*-
from utils.utils import get_data_from_url,get_link, get_title_from, get_domain
from utils.summarizer import summarizer


# # data = get_link(url)
# # for url in data:
# #     print("link ", url)
# #     try:
# #         print(get_data_from_url(url))
# #     except:
# #         print("error")

url = "https://www.nytimes.com/live/2020/11/03/us/trump-biden-election?action=click&module=Spotlight&pgtype=Homepage" 
data = get_data_from_url(url)
title = get_title_from(url)
domain = get_domain(url)

summarizer = summarizer(data,2)
print(domain)
print(title)
print(summarizer)

# from newspaper import Article
# # url = "https://medium.com/topic/popular"
# article = Article(url)
# print(article.download())

