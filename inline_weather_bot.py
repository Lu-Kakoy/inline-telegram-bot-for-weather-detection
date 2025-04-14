from bs4 import BeautifulSoup
import requests
import telebot
from telebot.types import *

token1 = 'TOKEN'
bot1 = telebot.TeleBot(token1)

class Weather:
    def __init__(self, link1):
        self.link = link1
        code_page = requests.get(self.link).text
        self.soup = BeautifulSoup(code_page, 'html.parser')
    def list_of_sites(self):
        links = self.soup.find_all('a')
        data = {}
        for i in links:
            text = i.__str__()
            name = i.get_text()
            text = text[text.find('href="'):][6:]
            last = text.find('"')
            text = text[:last]
            if name not in ('Мобильная версия', 'Главная', 'О сайте', 'Частые вопросы (FAQ)', 'Контакты',
                            'Литва', 'Беларусь', 'Россия', 'Украина', 'Все страны', '>>>', 'См. на карте',
                            '', 'Москва', 'на Сахалине', 'в Погиби', 'в Красноярском крае', #'Москва (ВДНХ)',
                            'в Норильске / им. Н. Н. Урванцева (аэропорт)', 'на Камчатке', 'в Усть-Камчатске (аэропорт)',
                            'в Республике Саха (Якутии)', 'в Анабаре', 'в Краснодарском крае', 'в Сочи / им. В. И. Севастьянова (аэропорт)',
                            'Адыгея', 'Алтайский край', 'Амурская область', 'Башкортостан', 'Старый Оскол', 'Бурятия', 'Улан-Удэ', 'Дагестан',
                            'Еврейская АО', 'Забайкальский край', 'Ингушетия', 'Кабардино-Балкария', 'Калмыкия', 'Камчатский край',
                            'Петропавловск-Камчатский', 'Карачаево-Черкесия', 'Карелия', 'Коми', 'Крым', 'Кузбасс', 'Ленинградская обл.',
                            'Марий Эл', 'Йошкар-Ола', 'Мордовия', 'Шереметьево / им. А. С. Пушкина (аэропорт)', 'Московская область',
                            'Нижний Новгород', 'Новгородская область', 'Великий Новгород', 'Приморье', 'Великие Луки', 'Республика Алтай',
                            'Горно-Алтайск', 'Республика Саха (Якутия)', 'Ростов-на-Дону', 'Санкт-Петербург', 'Сахалинская область',
                            'Южно-Сахалинск', 'Свердловская область', 'Северная Осетия-Алания', 'Татарстан', 'Тыва', 'Удмуртия',
                            'Комсомольск-на-Амуре', 'Хакасия', 'Ханты-Мансийск', 'Чечня', 'Чувашия', 'Чукотка',
                            'Ямало-Ненецкий автономный округ', 'Москва (центр, Балчуг)', 'Москва (юго-запад, МГУ)',
                            'в Магаданской области', 'на мысе Братьев', 'на мысе Стерлегова', 'на о. Тройной', 'в Делянкире'):
                data[name] = "https://rp5.ru" + text
        return data
@bot1.inline_handler(func=lambda query: len(query.query) > 0)
def inline1(query):

    link1 = city1(query.query)
    if link1 == 'None':
        ansver1 = InlineQueryResultArticle('1', 'ошибка!', description=f'не удалось найти город!', input_message_content=InputTextMessageContent(f'не удалось найти город!'),
thumbnail_url='https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Fgas-kvas.com%2Fgrafic%2Fuploads%2Fposts%2F2024-01%2Fgas-kvas-com-p-nadpis-error-na-prozrachnom-fone-15.png&text=ошибка&rpt=simage&lr=11327')
        bot1.answer_inline_query(query.id, [ansver1])
        return
    else:
        try:
            weather = Weather(link1)
            data2 = weather.soup.find("div", {"id": "archiveString"})
            data3 = data2.find("span",{"class":"t_0"}).text
            if data3 is None:
                data3 = data2.find('div', {'class': 'ArchiveInfo'})
            data4 = data2.find('a', {'class': 'ArchiveStrLink'})
            if data4 is None:
                data4 = data2.find('div', {'class': 'ArchiveInfo'})
            data4 = data4.text.replace('Архив погоды на метеостанции', ' ')
            data2 = weather.soup.find('div', {'id': "forecastShort", 'class': "round-5"})
            data5 = data2.find('b')
            data6 = data5.find('span', {'class': 't_0'}).text
            data6 = f'Сегодня ожидается {data6[:-3]}'
            data5 = str(data5)
            print(data5)
            data7 = data5[268:295]
            ansver1 = InlineQueryResultArticle('1', f'{query.query}: {data3}', description=data4, input_message_content=InputTextMessageContent(f'{query.query}: {data3}\n{data4}\n\n{data6}\n{data7}'))
            bot1.answer_inline_query(query.id, [ansver1])
        except:
            ansver1 = InlineQueryResultArticle('1', 'ошибка!', description=f'не удалось найти город!', input_message_content=InputTextMessageContent(f'не удалось найти город!'),
            thumbnail_url='https://yandex.ru/images/search?pos=8&from=tabbar&img_url=https%3A%2F%2Fsun9-2.userapi.com%2Fimpf%2Fc636623%2Fv636623188%2F5e141%2FjGXmSkx768E.jpg%3Fsize%3D1280x956%26quality%3D96%26sign%3De93bf5c4c67c8f4a12bb9abd6b7d9f25%26c_uniq_tag%3DCllvIVdzlumMiamLxvRB2IrZzLGWxUCRJFOVekG2fSM%26type%3Dalbum&text=ошибка&rpt=simage&lr=11327')
            bot1.answer_inline_query(query.id, [ansver1])

def city1(city):
    city = city.capitalize()
    weather = Weather('https://rp5.ru/Погода_в_России')
    data = weather.list_of_sites()
    link1 = 'None'
    for i in data.keys():
        if i in city:
            link1 = data[i]
    return link1



bot1.infinity_polling()






