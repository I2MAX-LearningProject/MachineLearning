# Day_03_07_meals.py
import re
import requests

def showMeals(year, month):
    # url = 'http://www.songok.es.kr/segio/meal_v2/meal_month.php?year=2016&month=11'

    root  = 'http://www.songok.es.kr/segio/meal_v2/meal_month.php?'
    # url   = root + 'year=' + '2016' + '&month=' + '11'
    # url   = root + 'year=' + str(year) + '&month=' + str(month)
    url = '{}year={}&month={}'.format(root, year, month)
    recvd = requests.get(url)
    # print(recvd)
    # print(recvd.text)

    meals = re.findall(r'<div class="meal_cont"><a href.+?</a>',
                       recvd.text, re.DOTALL)
    print(len(meals))

    for meal in meals:
        date = re.findall(r'name="(.+?)"',
                          meal, re.DOTALL)
        # print(date[0])
        # print(date[0].split(','))
        year, month, day, hour = date[0].split(',')

        # ---------------------------------------- #

        menu = re.findall(r'name=.+?>(.+?)</a>',
                          meal, re.DOTALL)
        # print(menu)

        menu_text = 'No menu.'

        if menu:
            # a = re.findall(r'\([0-9]+\)', menu[0], re.DOTALL)
            # print(a)
            menu_text = re.sub(r'\([0-9]+\)', '', menu[0], re.DOTALL)
            menu_text = re.sub(r'<br />', '', menu_text)
            menu_text = re.sub(r'\n', ',', menu_text)
            menu_text = re.sub(r'/', ',', menu_text)
            menu_text = re.sub(r',,', ',', menu_text)
            menu_text = re.sub(r'ㆍ', '', menu_text)
            menu_text = re.sub(r'\([0-9]+\)', '', menu_text)

        # ---------------------------------------- #

        print('{}.{}.{}] {}'.format(year, month, day, menu_text))


    # <div class="meal_cont"><a href="meal_view.php" id="meal_595" name="2016,11,16,2">하이라이스(2)(5)(6)(10)<br />
    # (12)(16)<br />
    # 닭다리양념구이(5)(6)(12)<br />
    # (15)<br />
    # 양상추샐러드/블루베리드레싱(2)(12)<br />
    # 깍두기(9)(17)(18)<br />
    # 희망우유(2)<br />
    # </a>

def showMealsForYear(year):
    for i in range(12):
        showMeals(year, i+1)


for y in range(2015, 2017):
    showMealsForYear(y)

