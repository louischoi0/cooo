import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from b import push
from time import sleep
import sys

def req(url):
    a = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2"
    b = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    headers = {
        "User-Agent": b,
        "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    }    

    res = requests.get(url, headers=headers)
    return BeautifulSoup(res.text, "lxml")

def get_items(soup):
    return soup.find_all("a", {"class": "search-product-link"})

def get_product_id_url(url):
    p = urlparse(url)
    return parse_qs(p.query)

def get_view_page(keyword, item_id):
    url = f"https://www.coupang.com/np/search?q={keyword}&channel=recent"
    item_id = str(item_id)
    print(url)
    soup = req(url)

    items = soup.find_all("a", {"class": "search-product-link"})
    pagenation = soup.find("a", {"class": "btn-last"})
    pagenum = int(pagenation.text)

    for p in range(pagenum):
        _url = url + f'&page={p}'
        print(_url)
        soup = req(_url)
        items = get_items(soup)
        print(len(items))
        for idx, i in enumerate(items):
            iurl = i["href"]
            name = i.find("div", {"class": "name"})
            print(name)
            query = get_product_id_url(iurl)
            _item_id = query["itemId"][0]
            _item_id = str(_item_id)
            print(_item_id) 
            if item_id == _item_id:

                return idx, p
    return -1, -1

if __name__ == "__main__": 

    while True:
        keyword = sys.argv[1]
        productid = int(sys.argv[2])
        idx, p = get_view_page(keyword,productid)

        if p:
            push(productid, keyword, p, idx)
            print(idx, p)

        sleep(60)

