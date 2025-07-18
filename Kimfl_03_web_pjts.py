# 1. 파이썬 웹크롤링 멜론 TOP100 실시간 차트순위 검색결과 가져오기 - beautifulsoup, requests 기초 사용법
# https://blog.naver.com/kimflstudio/222904659059
# https://www.youtube.com/watch?v=-oS3ItSbTcc 

# from bs4 import BeautifulSoup
# import requests

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
# }

# url = "https://www.melon.com/chart/index.htm"

# r = requests.get(url, headers=headers)

# print(r.raise_for_status)

# html = r.text

# soup = BeautifulSoup(html, "html.parser")

# lst50 = soup.select(".lst50")

# lst100 = soup.select(".lst100")

# lst = lst50 + lst100

# print(len(lst))

# for e, i in enumerate(lst, 1):
#     print(f"<<{e}위>>")
#     title = i.select_one(".ellipsis.rank01 a")
#     print(title.text)

#     singers = i.select(".ellipsis.rank02 > a")
#     for singer in singers:
#         print(singer.text)

#     album = i.select_one(".ellipsis.rank03 > a")
#     print(album.text)

#     print()
    
# 2. 파이썬 독학 selenium, beautifulsoup 사용법 기초 - 셀레니움 네이버 크롤링|작성자 김플
# https://www.youtube.com/watch?v=FVA_lqbqWiM
# https://blog.naver.com/kimflstudio/222899535081

from bs4 import BeautifulSoup
from selenium import webdriver
import time

base_url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="

keyword = input("검색어를 입력하세요 : ")

search_url = base_url + keyword

driver = webdriver.Chrome()

driver.get(search_url)

time.sleep(3)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

# items = soup.select(".api_txt_lines.total_tit")

# for e, item in enumerate(items, 1):
#     print(f"{e} : {item.text}")

items = soup.select(".total_wrap.api_ani_send")

for rank_num, item in enumerate(items, 1):
    print(f"<<{rank_num}>>")
    ad = item.select_one(".link_ad")
    if ad:
        print("광고입니다.")
        continue

    blog_title = item.select_one(".sub_txt.sub_name").text
    print(f"{blog_title}")

    post_title = item.select_one(".api_txt_lines.total_tit._cross_trigger")
    print(f"{post_title.text}")

    print(f"{post_title.get('href')}")
    print(f"{post_title['href']}")

    print()

driver.quit()