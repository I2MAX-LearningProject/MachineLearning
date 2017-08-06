# Day_05_06_songs.py
import requests
import re

def showSongs(code, page):
    # S_PAGENUMBER:4
    # S_MB_CD:W0726200
    # S_HNAB_GBN:I
    # hanmb_nm:권지용

    # payload = dict(S_MB_CD='W0726200', S_PAGENUMBER=1)
    payload = dict(S_MB_CD=code, S_PAGENUMBER=page)

    url = 'https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
    recvd = requests.post(url, data=payload)
    # print(recvd)
    # print(recvd.text)

    tbody = re.findall(r'<tbody>(.+?)</tbody>',
                       recvd.text, re.DOTALL)
    # print(tbody[0])

    tbody = re.sub(r' <img .+? />', '', tbody[0])
    tbody = re.sub(r'<br/>', ',', tbody)

    trs = re.findall(r'<tr>(.+?)</tr>',
                     tbody, re.DOTALL)
    # print(len(trs))

    if not trs:
        return False

    for tr in trs:
        # print(tr)
        tds = re.findall(r'<td>(.*?)</td>', tr)     # empty tag <td></td> 때문에 * 사용
        tds = [i.strip() for i in tds]
        print(tds)
        # print(len(tds))

    return True

# page = 1
# while showSongs('W0726200', page):
#     print('---------{}---------'.format(page))
#     page += 1

showSongs('W0726200', 1)







