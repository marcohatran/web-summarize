from utils.utils import get_data_from_url,get_link
from utils.summarizer import summarizer


# # data = get_link(url)
# # for url in data:
# #     print("link ", url)
# #     try:
# #         print(get_data_from_url(url))
# #     except:
# #         print("error")

url = "https://www.foxnews.com/us/portland-riot-declared-after-molotov-cocktails-tossed" 
data = get_data_from_url(url)
summarizer = summarizer(data,2)
print(summarizer)

# from newspaper import Article
# # url = "https://medium.com/topic/popular"
# article = Article(url)
# print(article.download())

