from utils.utils import get_data_from_url,get_link

url = r"https://medium.com/topic/popular"
data = get_link(url)
for url in data:
    print("link ", url)
    try:
        print(get_data_from_url(url))
    except:
        print("error")