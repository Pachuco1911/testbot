import requests
from bs4 import BeautifulSoup

def f(x):
    switcher = {
        0: 'ПОНЕДЕЛЬНИК:\n',
        1: 'ВТОРНИК:\n',
        2: 'СРЕДА:\n',
        3: 'ЧЕТВЕРГ:\n',
        4: 'ПЯТНИЦА:\n',
        5: 'СУББОТА:\n',
        6: 'ВОСКРЕСЕНЬЕ:\n'
        }
    return switcher.get(x)

def schedule(gr_num):
    text=''
    day_number = 0
    url = "https://petrsu.ru/schedule/term?group=" + str(gr_num)
    try:
        html = requests.get(url).text
        soup = BeautifulSoup (html, 'lxml')
        week = soup.find_all('div', class_='rTable')
        for day in week:
            line = f(day_number)
            day_number = day_number + 1
            try:
                lesson = day.find_all('div', class_='rTableRow')
                for part in lesson:
                    block = part.find_all('div', class_='rTableCell')
                    blocks = ''
                    for i in range(1, 5):
                        if i != 3:
                            blocks = blocks + block[i].text.strip().split('\t')[0].strip() + '\t'
                    line = line + blocks + '\n'
                text=text+line+'\n'
            except:
                line = ''
    except:
        text = ''
    return text



