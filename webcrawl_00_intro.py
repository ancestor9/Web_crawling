from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
# Selenium WebDriver 설정 및 Chrome 웹 드라이버 사용 (다른 브라우저도 사용 가능)
driver = webdriver.Chrome()

# 초기 URL로 이동
url = "https://news.naver.com/breakingnews/section/101/259"
driver.get(url)

# 페이지 내 모든 href 링크 수집
link_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href]')
links = [link.get_attribute('href') for link in link_elements]
# print(links)
# print(len(links))


# 기사에 해당하는 url만 가져오기
pattern = r'https://n\.news\.naver\.com/mnews/article/\d+/\d+'

## 기사 필터링
filtered_links = [link for link in links if re.match(pattern, link)]

## 중복된 것 제거
unique_links = list(set(filtered_links))


# 수집된 링크를 반복적으로 방문
for link in unique_links:
    # 각 URL로 이동
    driver.get(link)
    
    # 1초 대기 (필요한 경우 지연 시간 조절 가능)
    time.sleep(1)

# 작업 완료 후 웹 드라이버 종료
driver.quit()