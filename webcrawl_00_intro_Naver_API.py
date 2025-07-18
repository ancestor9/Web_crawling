# 네이버뉴스 API 공식문서 (네이버개발자센터)
# https://developers.naver.com/docs/serviceapi/search/news/news.md

#
# 네이버 검색 API 예제 - 블로그 검색
'''
https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EA%B2%80%EC%83%89-api-%EB%B8%94%EB%A1%9C%EA%B7%B8-%EA%B2%80%EC%83%89-%EA%B5%AC%ED%98%84-%EC%98%88%EC%A0%9C
'''
import os
import sys
import urllib.request

# https://developers.naver.com/apps/#/myapps/QyQOpD2t_b61Q96mF26Z/overview
client_id = "QyQOpD2t_b61Q96mF26Z"
client_secret = "abnz2iQulL"
encText = urllib.parse.quote("조상구교수")

'''
https://developers.naver.com/docs/common/openapiguide/apilist.md#%EB%B9%84%EB%A1%9C%EA%B7%B8%EC%9D%B8-%EB%B0%A9%EC%8B%9D-%EC%98%A4%ED%94%88-api
'''
# url = f"https://openapi.naver.com/v1/search/news?query={encText}&display=100"

url = "https://openapi.naver.com/v1/search/news?query=" + encText + "&display=" + str(100) # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)