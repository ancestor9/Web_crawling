
# 목차차
# 1. webdriver 자동 설치
# 2. trafilatura
# 3. 파이썬 beautifulsoup find, select 메소드 차이점
# 4. 파이썬 웹페이지 자동화를 위한 셀레니움 기초 입문


# https://www.youtube.com/@kimfl

# # 1. webdriver 자동 설치치
# from selenium import webdriver
# import time

# url = 'https://naver.com'

# driver = webdriver.Chrome()

# driver.get(url)
# time.sleep(3)

# # C:\Users\조근하\.cache\selenium\chromedriver 에 존재한다.

# 2. trafilatura
# pip install --upgrade trafilatura
import trafilatura

# url = 'https://news.kbs.co.kr/news/pc/main/main.html'
# # url = 'https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/' # kbs 뉴스
# downloaded = trafilatura.fetch_url(url)
# print(trafilatura.extract(downloaded))

from bs4 import BeautifulSoup

# url = 'https://www.ajunews.com/view/20250216212652363?l=N'
# html = trafilatura.fetch_url(url)

# print(type(html))

# soup = BeautifulSoup(html, "html.parser")
# # soup.select_one()
# result = trafilatura.extract(str(soup))
# print(type(soup))
# print(result)

# 3. 뷰티플수프의 웹크롤링 CSS Selector 사용법 (Not find)
# https://www.youtube.com/watch?v=HJcrD7Ukli4
html = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        .grape {color: purple;}
        .mango {color: yellow;}
        .banana {font-size: 30px;}
        .greenapple {color: green;}
    </style>
</head>
<body>
    <h1>CSS Selector</h1>
    <div id="site">
        <ul>
            <li><a class="apple" href="https://naver.com">네이버</a></li>
            <li><a class="grape" href="https://google.com">구글</a></li>
            <li><a class="mango" href="https://youtube.com">유튜브</a></li>
            <li><a class="greenapple" href="https://openai.com">OpenAI</a></li>
            <li><a class="greenapple" href="https://python.org">Python</a></li>
        </ul>
        <p class="apple">css selector를 설명하기 위한 페이지</p>
        <p class="apple banana">여기에는 두 개의 클래스가 사용</p>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")
# print(soup.select_one('h1'))
# print(soup.select_one('ul'))
# print(soup.select_one('#site')) # id
# print(soup.select_one('.apple')) # class
# print(soup.select('.apple')) # list
# print(soup.select('a.apple'))
# print(soup.select('p.apple'))
# print(soup.select('#site'))
# print(soup.select('#site ul'))
# print(soup.select('#site .apple')) # 자손 모두
# print(soup.select('#site > .apple')) # 자식만

# print(soup.select("p.apple"))

# print(soup.select("[class='apple']"))

# print(soup.select("p[class='apple']"))


# print(soup.select("a[class^=app]")) # app로 시작, 제일 많이 사용
# print(soup.select("a[class*=app]")) # app가 포함
# print(soup.select("a[class*=ppl]")) # app가 포함
# print(soup.select("a[class~=apple]")) # apple 만 정확히 포함, 제일 많이 사용

# print(soup.select("a[href$=org]")) # 끝에 org로 마침
# print(soup.select("a[href$='.org']")) # 끝에 org로 마침

# # print(soup.select(".apple banana"))

# print(soup.select(".apple.banana"))

# 3. 파이썬 beautifulsoup find, select 메소드 차이점
# https://www.youtube.com/watch?v=Xrf_DKSD3LY

html ='''<html>
<head>
    <style>
        ul {
            list-style: none;
        }
        a[href="https://naver.com"] {
            color: violet;
        }
        a[href*="google"] {
            color: skyblue;
        }
        #site > ul > li:nth-child(3) > a {
            color: green;
        }
        .liclass {
            font-size: 30px;
        }
    </style>
</head>
<body>
    <div id="site">
        <ul>
            <li><a href="https://naver.com">네이버</a></li>
            <li><a href="https://google.com">구글</a></li>
            <li class="liclass"><a href="https://youtube.com">유튜브</a></li>
        </ul>
    </div>
</body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")

# selector는 <style>의 css style의 포맷에 따라 <body> 내부에서 html구조를 기준으로 해당 태그를 찾아 요소를 선택한다.
# print(soup.select_one(".liclass"))
# print(soup.select_one("a[href='https://naver.com']"))
# print(soup.select_one("#site > ul > li:nth-child(3)"))
# print(soup.select_one("#site > ul > li:nth-child(3) > a"))
# # html크롬 화면에서 F12로 Copy > Copy Selector 하면 위의 명령어 안의 내용과 동일함 --> #site > ul > li.liclass > a
# # 그런데 이런 식으로 크롤링하면 안된다. 왜냐하며 ㄴ순서가 매 번 바뀔 수가 있다. 네이버 첫번쨰 화면 뉴스, 쇼핑, 등등

# print(soup.select_one("a[href^='https://naver.c']"))
# -------------------------------------------------------

# print(soup.find(class_="liclass"))
# print(soup.select_one('a', href='https://naver.com'))
# print(soup.find('a', href=lambda x: x and 'google' in x))

# import re
# print(soup.find('a', href=re.compile('google')))

# print(soup.select_one('a[href*="google"]'))

# 4. 파이썬 웹페이지 자동화를 위한 셀레니움 기초 입문
# https://www.youtube.com/watch?v=lgK0V4x2y2s


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# 검색 키워드를 입력받습니다.
# keyword = input("검색 키워드 입력: ")

# Chrome 브라우저 옵션 설정
options = Options()
options.add_argument("--start-maximized")  # 브라우저를 최대화된 상태로 엽니다.
options.add_experimental_option("detach", True)  # 스크립트 실행 후에도 브라우저를 닫지 않습니다.

# Chrome 웹드라이버를 설정된 옵션과 함께 시작합니다.
driver = webdriver.Chrome(options=options)

# 네이버 홈페이지로 이동합니다.
url = "https://naver.com"
driver.get(url)
time.sleep(3)  # 페이지가 로드될 시간을 기다립니다.

# 검색 입력창을 찾아서 검색 키워드를 입력합니다.
# By.~~~ chat 에게 문의의
query = driver.find_element(By.ID, "query") # 정적 웹인 경우 직관적임.
# element = driver.find_element(By.XPATH, '//*[@id="query"]')과 동일하나 정적으로 변경되는 경우
query.send_keys("빅데이터")

search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
search_btn.click()
time.sleep(2)  # 검색 결과 페이지가 로드될 시간을 기다립니다.

driver.save_screenshot("naver_빅데이터.png")
driver.quit()
# ------------------
# query.send_keys(f"{keyword}")
# time.sleep(2)  # 키워드 입력 후 잠시 기다립니다.

# 검색 입력창을 찾아서 검색 키워드를 입력합니다.
# By.~~~ chat 에게 문의의
# query = driver.find_element(By.ID, "query") # 정적 웹인 경우 직관적임.
# element = driver.find_element(By.XPATH, '//*[@id="query"]')과 동일하나 정적으로 변경되는 경우

# # 검색 버튼을 찾아서 클릭합니다.
# search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
# search_btn.click()
# time.sleep(2)  # 검색 결과 페이지가 로드될 시간을 기다립니다.

# # 현재 브라우저 화면을 스크린샷으로 저장합니다.
# driver.save_screenshot(f"naver_{keyword}.png")

# # 브라우저를 종료합니다.
# driver.quit()