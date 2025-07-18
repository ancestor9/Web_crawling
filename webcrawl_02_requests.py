'''
https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
'''

import requests


r = requests.get('https://api.github.com/events')
# print(r.text)

# 가독성있게 읽으려면면
import json
# JSON 데이터를 딕셔너리로 변환
data = r.json()

r = requests.post('https://httpbin.org/post', data={'key': 'value'})

r = requests.put('https://httpbin.org/put', data={'key': 'value'})
r = requests.delete('https://httpbin.org/delete')

r = requests.head('https://httpbin.org/get')
print(r.status_code)  # HTTP 응답 코드 출력
print(r.headers)  # 응답 헤더 출력
print(r.text)  # 응답 본문 출력 (HEAD 요청이므로 일반적으로 없음)
print("*"*100)

# 서버가 지원하는 HTTP 메서드 확인
r = requests.options('https://httpbin.org/get') 
print(r.status_code)  # HTTP 응답 코드 출력
print(r.headers)  # 응답 헤더 출력
print("*"*100)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)
print("*"*100)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.url)