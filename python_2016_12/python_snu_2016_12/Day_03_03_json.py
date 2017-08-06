# Day_03_03_json.py
import json

j1 = '{"ip": "8.8.8.8"}'
d1 = json.loads(j1)
print(d1)
print(type(d1))
print(d1['ip'])

j2 = '''{"Accept-Language": "en-US,en;q=0.8","Host": "headers.jsontest.com","Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}'''

# 문제
# j2를 해석해서 값(value)만 출력해 보세요.
d2 = json.loads(j2)
print(type(d2))
print(d2['Accept-Charset'])

for k, v in d2.items():
    print(k, v)

for k in d2:
    print(k, d2[k])
print('-'*50)

# load : string --> object
# dump : object --> string
j3 = json.dumps(d2)
print(j3)
print(type(j3))








