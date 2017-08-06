# Day_03_04_json_kma.py
import json
import requests

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
recvd = requests.get(url)
print(recvd.text)

text = bytes(recvd.text, 'iso-8859-1').decode('utf-8')
print(text)

# 문제
# 코드와 도시 이름만 출력해 보세요.
items = json.loads(text)
print(items)
print(type(items))

for item in items:
    print(item['code'], item['value'])
