# Day_04_01_translation.py
import requests
import json

def not_used():
    # Accept:*/*
    # Accept-Encoding:gzip, deflate
    # Accept-Language:ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4
    # Connection:keep-alive
    # Content-Length:236
    # content-type:application/x-www-form-urlencoded; charset=UTF-8
    # Cookie:npic=zAiceKejPrHjVaf0nAVhV173yzw7cI4PH3GGz9vRJVd03DGTkIu48Df82n4kKY5GCA==; NNB=ALGCGT7MAFVFQ; nx_ssl=2; NaverSuggestPlus=unuse; NaverSuggestUse=use%26use; wcs_bt=dccae51cc9ffb4:1483578203
    # Host:labspace.naver.com
    # Origin:http://labspace.naver.com
    # Referer:http://labspace.naver.com/nmt/
    # User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
    # x-naver-client-id:labspace

    headers = {'x-naver-client-id': 'labspace'}

    payload = dict(source='ko', target='en',
                   text='세상은 데이터를 가진 자와 갖지 않은 자로 나뉩니다.')

    url= 'http://labspace.naver.com/api/n2mt/translate'
    recvd = requests.post(url, data=payload, headers=headers)
    print(recvd)
    print(recvd.text)
    print(type(recvd.text))

    root = json.loads(recvd.text)
    print(type(root))
    print(root.keys())      # 'message'

    message = root['message']
    print(message)
    print(message.keys())   # '@service', '@type', '@version', 'result'

    result = message['result']
    print(result)
    print(result.keys())    # 'tarLangType', 'translatedText', 'srcLangType'
    print('-'*50)

    print(result['srcLangType'])
    print(result['tarLangType'])
    print(result['translatedText'])
    # The world is divided into those who have no data.


def translate(text, kor2eng):
    headers = {'x-naver-client-id': 'labspace'}
    payload = dict(source='ko', target='en', text=text)

    if not kor2eng:
        payload['source'] = 'en'
        payload['target'] = 'ko'

    url= 'http://labspace.naver.com/api/n2mt/translate'
    recvd = requests.post(url, data=payload, headers=headers)

    root = json.loads(recvd.text)
    message = root['message']
    result = message['result']

    return result['translatedText']

print(translate('파이썬을 계속 공부하는 방법이 있을까요?', True))
print(translate('Do you know how to keep up with python?', False))






