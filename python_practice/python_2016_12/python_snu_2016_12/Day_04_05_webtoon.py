# Day_04_05_webtoon.py
import requests
import re
import os

def saveImage(url, title):
    title = re.sub(r'\?', '', title)
    filename = 'Webtoon/{}.{}'.format(title, 'jpg')       # os.path.splitext(url)
    # print(filename)
    recvd = requests.get(url)

    f = open(filename, 'wb')
    f.write(recvd.content)
    f.close()


url = 'http://comic.naver.com/webtoon/weekday.nhn'
recvd = requests.get(url)
# print(recvd)
# print(recvd.text)

# 문제
# 요일별로 웹툰 제목과 썸네일 주소를 출력해 보세요.

weekdays = re.findall(r'<div class="col_inner">.+?</ul>', recvd.text, re.DOTALL)
# print(len(weekdays))

items = []
for index, day in enumerate(weekdays):
    # print(day)

    # li = re.findall(r'<li>.+?</li>', day, re.DOTALL)
    # print(len(li))

    item = re.findall(r'src="(.+?)".+?title="(.+?)"', day, re.DOTALL)
    # print(len(item))
    # print(*item, sep='\n')

    for i, (img, title) in enumerate(item):
        if not '.gif' in img:
            # print(i+1, img, title)
            names = ['월', '화', '수', '목', '금', '토', '일']
            items.append((names[index], img, title))
            # items.append(('월화수목금토일'[index], img, title))
            # items.append((index, img, title))
    # break
    # item = [(img, title) for img, title in item if not '.gif' in img]
    # print(len(item))

# print(*items, sep='\n')

if not os.path.exists('Webtoon'):
    os.mkdir('Webtoon')

for day, url, title in items:
    saveImage(url, title)






