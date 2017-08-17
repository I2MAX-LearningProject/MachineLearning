# Day_02_03_kma.py
import requests
import re

f = open('Data/kma.csv', 'w', encoding='utf-8')

# 엑셀에서 열고 싶을 때.
# f = open('Data/kma.csv', 'w')
# f = open('Data/kma.csv', 'w', encoding='cp949')

# ---------------------------- #

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
# print(recvd)
# print(recvd.text)

# temp = re.findall(r'<province>.+</province>', recvd.text)
# print(temp)
# print(len(temp))

# 문제
# 전체 location을 가져와 봅니다.
# 기본 : 탐욕적 greedy(.+)
#       비탐욕적 non-greedy(.+?)
locations = re.findall(r'<location wl_ver="3">.+?</location>',
                       recvd.text,
                       re.DOTALL)
# print(len(locations))

for loc in locations:
    # print(loc)

    # 문제
    # province를 찾아서 출력해 보세요.
    # city를 찾아서 출력해 보세요.
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    # print(prov[0], prov)
    # print(city[0])

    # # items = re.findall(r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>',
    # #                    loc, re.DOTALL)
    # items = re.findall(r'<mode>(.+?)<.+?>.+?<.+?>(.+?)<.+?>.+?<.+?>(.+?)<.+?>',
    #                    loc, re.DOTALL)
    # # print(items)
    # # print(len(items))
    #
    # # for item in items:
    # #     print(item)
    #
    # for mode, tmEf, wf in items:
    #     print(mode, tmEf, wf)




    # data를 찾아 보세요.
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(data)
    # print(len(data))


    for datum in data:
        # print(datum)

        # 문제
        # mode를 비롯한 나머지를 찾아 보세요.
        mode = re.findall(r'<mode>(.+?)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
        wf   = re.findall(r'<wf>(.+?)</wf>', datum)
        tmn  = re.findall(r'<tmn>(.+?)</tmn>', datum)
        tmx  = re.findall(r'<tmx>(.+?)</tmx>', datum)
        reli = re.findall(r'<reliability>(.+?)</reliability>', datum)
        # print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])

        row = '{},{},{},{},{},{},{},{}'.format(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])
        print(row)
        f.write(row)
        f.write('\n')

        # items = re.findall(r'<mode>(.+?)</mode>.+<tmEf>(.+?)</tmEf>.+<wf>(.+?)</wf>', datum, re.DOTALL)
        # # print(items[0])
        # print(items[0][0], items[0][1], items[0][2])
        # t = items[0]
        # print(t[0], t[1], t[2])


# 제주도 서귀포 A02 2017-01-06 00:00 구름많음 10 14 낮음
# 제주도 서귀포 A02 2017-01-06 12:00 구름많음 10 14 보통

# [('A01', '2017-01-13 00:00', '구름많음')]

# ---------------------------- #

f.close()
