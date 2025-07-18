'''
웹크롤링 비법 대공개! 데이터 수집 기초부터 돈버는 전략까지 한번에 배우기!
https://www.youtube.com/watch?v=Uf21RUo3KNc&list=PLNO7MWpu0eeUFdGMirV8_EkiLETqj8xA4&index=2

'''
# 연습
import requests

response = requests.get("https://startcoding.pythonanywhere.com/basic") # 객체 : 데이터 + 명령어
# print(response.status_code)
# print(response.text)


from bs4 import BeautifulSoup
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.select(".brand-name1")) # selector : 선택자
# print(soup.select(".brand-name")) # selector : 선택자
# print(soup.select_one(".brand-name")) # selector : 선택자
# print(soup.select_one(".brand-name").text) # selector : 선택자
# print(soup.select_one(".brand-name").attrs) # selector : 선택자
# print(soup.select_one(".brand-name").attrs['href']) # selector : 선택자


'''
실습
1. 한 개의 상품
2. 여러 개 상품
3. 여러 페이지
4. 엑셀이나 구글시트에 저장
'''

# step 1. 한 개의 상품
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.select_one(".product-category"))
# print(soup.select_one(".product-category").text)
# print(soup.select(".product-category"))

# print(soup.select_one(".product-name").text)
# print(soup.select_one(".product-name > a").attrs['href'].split('#')[1])

# print(soup.select_one(".product-price").text)
# print(len(soup.select_one(".product-price").text))
# print(soup.select_one(".product-price").text.split(' '))
# print(soup.select_one(".product-price").text.strip()) # 공백제거
# print(len(soup.select_one(".product-price").text.strip())) # 공백제거
# print(soup.select_one(".product-price").text.strip().replace(',','').replace('원', ''))

# category = soup.select_one(".product-category").text
# name = soup.select_one(".product-name").text
# link = soup.select_one(".product-name > a").attrs['href']
# price = soup.select_one(".product-price").text.strip().replace(',','').replace('원', '')

# print(category, name, link, price)

# step 2. 여러 개 상품
# 숲(전체 html)에서 나무(상품군)를 찾아 하나 하나 열매(상품)를 끝까지 (반목분으로)채취
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# items = soup.select(".product") # selector : 선택자에 매칭되는 tag 전체를 리스트로 반환,
# # print(items)
# for item in items:
#     category = item.select_one(".product-category").text
#     name = item.select_one(".product-name").text
#     link = item.select_one(".product-name > a").attrs['href']
#     # price = item.select_one(".product-price").text.split('원')
#     # price = item.select_one(".product-price").text.strip().replace(',','').replace('원', '') # 직접 확인?
#     price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
#     print(category, name, link, price)

# step 3. 여러 페이지 크롤링
# URL(Uniform Resource Locator)
# Protocol://Domain/Path?Parameter
# Parameter는 서버에 key:value 값으로 구체적으로 요청청
# https://search.naver.com/search.naver?where=news&query=삼성전자
# 여러 개 사이트 연습, 네이버웹툰, 네이버부동산, 네이버주가 등등

# 여러 페이지를 크롤링하는 방법, 리스트에서 골라서 클릭해보고, 직접 사이트에 가서 페이지 클릭해봐봐
# print([f"https://startcoding.pythonanywhere.com/basic?page={i}" for i in range(1, 5)])

# for i in range(1, 5):
#     response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.select(".product")
#     print(f'\n\n\n현재 크롤링 페이지는 {i} page {i*"*"}')
#     for item in items:
#         category = item.select_one(".product-category").text
#         name = item.select_one(".product-name").text
#         link = item.select_one(".product-name > a").attrs['href']
#         price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
#         print(category, name, link, price)

# step 4. 데이터프레임으로 만들고 엑셀로 내보내기(구글시트로 내보내기)

data = []
for i in range(1, 5):
    response = requests.get(f"https://startcoding.pythonanywhere.com/basic?page={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select(".product")
    # print(f'\n\n\n현재 크롤링 페이지는 {i} page {i*"*"}')
    for item in items:
        category = item.select_one(".product-category").text
        name = item.select_one(".product-name").text
        link = item.select_one(".product-name > a").attrs['href']
        price = item.select_one(".product-price").text.split('원')[0].replace(',', '')
        # print(category, name, link, price)
        data.append([category, name, link, price])
        
import pandas as pd
df = pd.DataFrame(data,
                    columns =['category', 'name', 'link', 'price'])
print(df.head(10))

df.to_excel('result.xlsx', index=False)