import subprocess
from urllib.parse import quote
from bs4 import BeautifulSoup as soup

# curl 명령어를 리스트 형태로 구성

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

def get_item_list_body(keyword, page):
    command = get_curl_command(keyword, page)
    # subprocess.run() 함수를 사용하여 명령어 실행
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout


if __name__  == "__main__":
    r = get_item_list_body('장어', 1)
    s = soup(r, parser='lxml')
    print(s)
