'''
chatgpt1 : 
https://www.google.com/search?q=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&sca_esv=7833c6f0638101e1&biw=1396&bih=632&tbm=nws&sxsrf=AHTn8zoPLw-s-Auk_YJk7JJ-5KUrb0ILLw%3A1740004958862&ei=Xl62Z7iwNPGUvr0Pj4eruQY&ved=0ahUKEwi41-vL59CLAxVxiq8BHY_DKmcQ4dUDCA4&uact=5&oq=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&gs_lp=Egxnd3Mtd2l6LW5ld3MiDOu4lOueme2Vke2BrDIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARIxUZQxAhYmENwA3gAkAECmAHlAaABpRWqAQYwLjE2LjG4AQPIAQD4AQGYAg2gAt4OqAIAwgIEEAAYA8ICBxAAGIAEGAqYAwOIBgGSBwUyLjkuMqAH9Vg&sclient=gws-wiz-news

url 페이지에서 아래 class에 해당되는 모든 기사를 추출하려고한다.
<div class="n0jPhd ynAwRc tNxQIb nDgy9d" aria-level="3" role="heading" style="-webkit-line-clamp:3">[단독] 김건희가 블랙핑크 막았다? 백악관 공연 무산 진실</div>

파이썬 코드를 다옹
'''

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time

# # Selenium WebDriver 설정
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # 브라우저 창을 띄우지 않음
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service, options=options)

# # Google 뉴스 검색 URL
# url = "https://www.google.com/search?q=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&sca_esv=7833c6f0638101e1&biw=1396&bih=632&tbm=nws"

# driver.get(url)
# time.sleep(3)  # 페이지 로딩 대기

# # 페이지 소스 가져오기
# soup = BeautifulSoup(driver.page_source, "html.parser")

# # 특정 클래스에 해당하는 기사 추출
# articles = soup.find_all("div", class_="n0jPhd ynAwRc tNxQIb nDgy9d")

# # 기사 제목 출력
# for idx, article in enumerate(articles, start=1):
#     print(f"{idx}. {article.text.strip()}")

# # 드라이버 종료
# driver.quit()


'''
정적웹페이지를 가정하고 selenium을 사용하지 말고 크롤링하는 코드를 제시해줘
'''

#------------ 정적 web
# import requests
# from bs4 import BeautifulSoup

# # Google 뉴스 검색 URL (정적 웹페이지라고 가정)
# url = "https://www.google.com/search?q=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&tbm=nws"

# # HTTP 요청 헤더 설정 (Google이 자동 크롤링을 차단하는 경우 우회)
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }

# # 페이지 요청 및 HTML 가져오기
# response = requests.get(url, headers=headers)
# if response.status_code != 200:
#     print("페이지 요청 실패:", response.status_code)
#     exit()

# # HTML 파싱
# soup = BeautifulSoup(response.text, "html.parser")

# # 특정 class를 가진 기사 제목 찾기
# articles = soup.find_all("div", class_="n0jPhd ynAwRc tNxQIb nDgy9d")

# # 기사 제목 출력
# for idx, article in enumerate(articles, start=1):
#     print(f"{idx}. {article.text.strip()}")

'''
soup.find_all("div", class_="n0jPhd ynAwRc tNxQIb nDgy9d") 대신 select 문을 사용하면 이 코드만 변경해줘
'''

# 특정 class를 가진 기사 제목 찾기 (CSS 선택자 사용)
articles = soup.select("div.n0jPhd.ynAwRc.tNxQIb.nDgy9d")

# 기사 제목 출력
for idx, article in enumerate(articles, start=1):
    print(f"{idx}. {article.text.strip()}")
