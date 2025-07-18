import requests

r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))

print(r.status_code)
print('\n')

print(r.headers)
print('\n')

print(r.headers['Content-Type'])
print('\n')

print(r.encoding)
print('\n')

print(r.text)
print(type(r.text))
print('\n')

print(r.json())
print(type(r.json()))