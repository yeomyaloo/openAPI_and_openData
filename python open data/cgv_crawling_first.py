from bs4 import BeautifulSoup
import requests

#리퀘스트 모듈로 원하는 날짜에 cgv 상영 시간표 가져오기
url = "https://www.lottecinema.co.kr/NLCHS/Cinema/Detail?divisionCode=1&detailDivisionCode=1&cinemaID=1005"
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
a = soup.select_one('div.mCustomScrollbar')
if a:
    title = a.select_one('div.list_tit > p').text.strip()
    print(title)
