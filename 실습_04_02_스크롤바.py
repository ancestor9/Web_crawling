from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-fullscreen')

# WebDriver 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Google 이미지 검색 페이지 열기
url = "https://www.google.com/search?q=cat&tbm=isch"
driver.get(url)
time.sleep(3)  # 초기 로딩 대기

# 스크롤을 반복해서 내려서 더 많은 이미지를 로드
scroll_pause_time = 3  # 3초 대기
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)  # 데이터 로딩 대기

    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break  # 더 이상 로드할 데이터가 없으면 종료
    last_height = new_height

# WebDriver 종료
driver.quit()

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-fullscreen')

# WebDriver 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
url = 'https://new.land.naver.com/complexes/111515?ms=37.4983893,127.1105193,16&a=APT:PRE:ABYG:JGC&e=RETAIL'
driver.get(url)
time.sleep(5)  # 페이지 로딩 대기

# 스크롤 대상 요소 찾기
try:
    scrollable_element = driver.find_element(By.ID, "articleListArea")  # ID를 정확히 확인
except:
    scrollable_element = driver.find_element(By.CLASS_NAME, "infinite_scroll")  # 대체 요소 찾기

# ActionChains를 사용하여 스크롤
actions = ActionChains(driver)
scroll_pause_time = 3  # 3초 대기
scroll_step = 500  # 한 번에 스크롤할 길이 (픽셀)

last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)
current_scroll = 0  # 현재 스크롤 위치

while current_scroll < last_height:
    driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", scrollable_element, scroll_step)
    time.sleep(scroll_pause_time)  # 데이터 로딩 대기
    current_scroll += scroll_step
    
    # 새로운 높이 확인
    new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)
    if current_scroll >= new_height:
        break

# WebDriver 종료
driver.quit()

# 네이버 부동산이 동적 요소를 강하게 사용하고 있어서 document.body.scrollHeight 방식이 적용되지 않을 가능성이 높아
'''