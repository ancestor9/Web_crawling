'''
from bs4 import BeautifulSoup
import requests

url ='https://new.land.naver.com/complexes/111515?ms=37.4983893,127.1105193,16&a=APT:PRE:ABYG:JGC&e=RETAIL'

# Fetch the HTML content from the URL
response = requests.get(url)  
html = response.content  

soup = BeautifulSoup(html, 'html.parser')

# item_inner 클래스를 가진 모든 element 찾기
items = soup.find_all(class_="item_inner")

동적 콘텐츠: 네이버 부동산 웹페이지는 JavaScript를 사용하여 동적으로 콘텐츠를 로드하는 경우로로
requests.get()으로 가져오는 HTML 소스 코드에는 JavaScript가 실행되기 전의 초기 HTML만 포함되어 있기 떄문에에
따라서 item_inner 클래스를 가진 요소가 초기 HTML에는 존재하지 않아 BeautifulSoup이 찾지 못하는 것
------> selenium으로 동적 web을 가져와야 한다.
- https://www.youtube.com/watch?v=ltXV7dng3Gs 
'''


# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-fullscreen')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url ='https://new.land.naver.com/complexes/111515?ms=37.4983893,127.1105193,16&a=APT:PRE:ABYG:JGC&e=RETAIL'
driver.get(url=url)
time.sleep(5) # 10초추 자동 close

# perplexity ai로 
'''
<div class="item_inner "><a href="javascript:void(0);" ---> copy elelemt 한 후
여기서 <div class="item_inner "> 안에 있는 모든 element를 골라내려고 한다. 어떤 명령어를 사용하여야 하나?
아래 코드를 답변으로 준다.
'''
# item_inner 클래스를 가진 모든 element 찾기
items = driver.find_elements(By.CLASS_NAME, "item_inner")

for item in items:
    # print(item)
    print(item.find_element(By.CLASS_NAME, "item_title").text)

# 찾은 element들을 순회하며 필요한 정보 추출 (예시)
for item in items:
    # item_title 클래스를 가진 element 찾기
    try:  # 예외 처리 추가
        title_element = item.find_element(By.CLASS_NAME, "item_title")
        title = title_element.text
        print("Title:", title)
    except:
        print("Title element not found in this item.")

    # price 클래스를 가진 element 찾기
    try:  # 예외 처리 추가
        price_element = item.find_element(By.CLASS_NAME, "price")
        price = price_element.text
        print("Price:", price)
    except:
        print("Price element not found in this item.")

    # 추가적인 element 추출 (예: 아파트 종류, 면적 등)
    try:
        info_area = item.find_element(By.CLASS_NAME, "info_area")
        spec_lines = info_area.find_elements(By.TAG_NAME, "p")
        for line in spec_lines:
            print(line.text)
    except:
        print("Info area not found in this item.")

    print("-" * 20)  # 구분선

# WebDriver 종료
driver.quit()

# ---------- 여기까지 코드를 제시해준다.