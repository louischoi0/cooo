import requests
from bs4 import BeautifulSoup as soup
from urllib.parse import quote
from urllib.parse import urlparse, parse_qs
import subprocess

import boto3
from boto3.dynamodb.conditions import Key
import pandas as pd

dynamodb = boto3.resource(
    'dynamodb',
)

def push(item_id, keyword, page, idx):
    table = dynamodb.Table('cooviewhistory')

    now = pd.Timestamp.now()
    table.put_item(
         Item={
          'logts': int(now.timestamp()),
          'item_id': int(item_id),
          'page': int(page),
          'idx': int(idx),
          'keyword': str(keyword),
          'dt': now.isoformat(),
      }
    )

def req(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
    res = requests.get(url, headers=headers)
    return soup(res.text, "lxml")

def get_items(soup):
    return soup.find_all("a", {"class": "search-product-link"})

def get_product_id_url(url):
    p = urlparse(url)
    return parse_qs(p.query)

def get_view_page_requests(keyword, item_id):
    url = f"https://www.coupang.com/np/search?q={keyword}&channel=recent"
    item_id = str(item_id)
    print(url)
    soup = req(url)
    return _get_view_page(soup, keyword, item_id)

def get_curl_command(keyword, page):
    encoded_string = quote(keyword)
    
    command = [
    "curl",
    f"https://www.coupang.com/np/search?q={encoded_string}&channel=recent&page={page}",
    "--compressed",
    "-H", "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "-H", "Accept-Language: ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
    "-H", "Accept-Encoding: gzip, deflate, br",
    "-H", "Connection: keep-alive",
    "-H", "Upgrade-Insecure-Requests: 1",
    "-H", "Sec-Fetch-Dest: document",
    "-H", "Sec-Fetch-Mode: navigate",
    "-H", "Sec-Fetch-Site: cross-site",
    "-H", "Pragma: no-cache",
    "-H", "Cache-Control: no-cache",
    "-H", "TE: trailers"
    ]

    return command


def get_item_list_page(keyword, page):
    command = get_curl_command(keyword, page)
    # subprocess.run() 함수를 사용하여 명령어 실행
    result = subprocess.run(command, capture_output=True, text=True)
    body = result.stdout
    return soup(body, parser='lxml')

def get_view_page_curl(keyword, item_id):
    s = get_item_list_page(keyword, 0)
    return _get_view_page(s, keyword, item_id, get_item_list_page)

def _get_view_page(soup, keyword, item_id, req_call_func):
    items = soup.find_all("a", {"class": "search-product-link"})
    pagenation = soup.find("a", {"class": "btn-last"})
    pagenum = int(pagenation.text)

    for p in range(pagenum):
        soup = req_call_func(keyword, p)
        items = get_items(soup)

        for idx, i in enumerate(items):
            iurl = i["href"]
            name = i.find("div", {"class": "name"})
            query = get_product_id_url(iurl)
            _item_id = query["itemId"][0]
            _item_id = str(_item_id)
            print(_item_id) 
            if item_id == _item_id:
                return idx, p


def _item_schedule_func(keyword, item_id):
    idx, p = get_view_page_curl(keyword, item_id)
    push(productid, keyword, p, idx)

if __name__ == "__main__": 
    keyword = "장어"
    productid = 21842068713
    idx, p = get_view_page_curl(keyword,productid)
    print(idx, p)
