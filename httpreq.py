import subprocess

# curl 명령어를 리스트 형태로 구성
command = [
    "curl",
    "https://www.coupang.com/np/search?q=%EC%9E%A5%EC%96%B4&channel=recent",
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

# subprocess.run() 함수를 사용하여 명령어 실행
result = subprocess.run(command, capture_output=True, text=True)

# 출력 결과 확인
print(result.stdout)

