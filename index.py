import telebot
from telebot import types
import requests
import pandas as pd
import time

bot = telebot.TeleBot('1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0')
port = ""
month = ""
day = ""
direct = ""
timeP = []
number_Flight = []
term = []
plat = []
mod = []
comp = []
rightAns = ''
helper = ''
userchange = '' #в аэропорт или из аэропорта (in, from)
tarif = ''
help1 = ''
help2 = ''
help3 = ''
help4 = ''
help5 = ''
help6 = ''
geoloc = ''
#@bot.message_handler(content_types=['text'])
#def names(m):
 #   if m.text == u"\u2708" + 'Информация о рейсе' or m.text == u"\U0001F4BB" + 'Разработчики':
   #     name(m)
  #  else:
   #     start(m)

@bot.message_handler(content_types=['text'])
#после перезагрузки бота, если у пользователя все еще открыта клавиатура, она не будет работать. возвращаем его к /start
def reanimator(m):
    if m.text != '/start':
        bot.send_message(m.chat.id, 'Упс, похоже ваши данные были утеряны. Пожалуйста, повторите ввод.')
        start(m)
    else:
        start(m)

def start(m):
    msg = bot.send_message(m.chat.id, "Привет, я Aerohelper. Давай посмотрим список доступных команд.")
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.add(
        *[types.KeyboardButton(name) for name in [u"\u2708" + 'Информация о рейсе', u"\U0001F4BB" + 'Разработчики']])
    keyboard.add(
        *[types.KeyboardButton(name) for name in
          ['Гид по аэропорту', 'Поиск отеля', 'Вызов такси']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, printPort)


def printPort(m):
    global helper
    if m.text == u"\U0001F4BB" + 'Разработчики':
        printDev(m)
    elif m.text == u"\u2708" + 'Информация о рейсе':
        keyboard1 = types.ReplyKeyboardMarkup(True, True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, inputPort)
    elif m.text == 'Гид по аэропорту':
        helper = '1'
        keyboard1 = types.ReplyKeyboardMarkup(True, True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, inputPort)
    elif m.text == 'Вызов такси':
        helper = '2'
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.add(*[types.KeyboardButton(name) for name in ['Из аэропорта', 'В аэропорт']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери, что тебе нужно', reply_markup=keyboard)
        bot.register_next_step_handler(msg, inputPort)


    elif m.text == 'Поиск отеля':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Отели рядом с Домодедово", url="https://www.booking.com/searchresults.ru.html?aid=335789;label=DME-KXeUEPj%2ApD_UkZq%2AZuGD4AS408332454365%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-21825927579%3Alp9047026%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YXL5GV3cgz10tAy2wcQyJHo;sid=1ac49a740e43dd8ad82c27e22ac23416;airport=187;from_airport=1;keep_landing=1;redirected=1;source=airport&gclid=Cj0KCQjw-r71BRDuARIsAB7i_QOgEO8XBh7IkJJ2ZdLB6KxdOb9adtwVWo8bXujlUMtXklMptpnAfOMaAkggEALw_wcB&"))
        bot.send_message(m.chat.id, "Выбери, что тебе интересно.", reply_markup=markup)



def printDev(m):
    smile = u'\U0001F525'
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
    msg = bot.send_message(m.chat.id, smile + 'by egorov dynasty', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputPort)


def inputPort(m):
    global port, userchange
    if m.text == u"\U0001F519" + 'Назад':
        global helper
        helper = ''
        start(m)
        return

    elif helper == '2':
        if m.text == 'Из аэропорта':
            userchange = 'from'
        else:
            userchange = 'in'
        portt(m)
    else:
        port = m.text
        if helper == '1':
            guideMenu(m)

        else:
            printMonth(m)



def guideMenu(m):
    global helper
    helper = ''
    if port == 'Домодедово':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Схема аэропорта", url="https://www.dme.ru/airportguide/map/"))
        markup.add(types.InlineKeyboardButton(text= u"\U0001F30C" + " Карта 2gis(навигация и метки магазинов)", url="https://go.2gis.com/ppqe5"))
        markup.add(types.InlineKeyboardButton(text=u"\U0001F4DC" + " История", url='https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BC%D0%BE%D0%B4%D0%B5%D0%B4%D0%BE%D0%B2%D0%BE_(%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82)'))
        bot.send_message(m.chat.id, "Выбери, что тебе интересно.", reply_markup=markup)
    elif port == 'Шереметьево':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Схема аэропорта", url="https://www.svo.aero/ru/map?terminal=all"))
        markup.add(types.InlineKeyboardButton(text= u"\U0001F30C" + " Карта 2gis(навигация и метки магазинов)", url="https://2gis.ru/moscow/search/%D0%A8%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%82%D1%8C%D0%B5%D0%B2%D0%BE%20%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82?floor=3&m=37.413421%2C55.980691%2F17.42"))
        markup.add(types.InlineKeyboardButton(text=u"\U0001F4DC" + " История", url='https://ru.wikipedia.org/wiki/%D0%A8%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%82%D1%8C%D0%B5%D0%B2%D0%BE'))
        bot.send_message(m.chat.id, "Выбери, что тебе интересно.", reply_markup=markup)
    elif port == 'Внуково':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Схема аэропорта", url="http://www.vnukovo.ru/airport-map/"))
        markup.add(types.InlineKeyboardButton(text= u"\U0001F30C" + " Карта 2gis(навигация и метки магазинов)", url="https://2gis.ru/moscow/firm/4504127919441635?floor=3&m=37.286956%2C55.606092%2F18.12"))
        markup.add(types.InlineKeyboardButton(text=u"\U0001F4DC" + "История", url='https://ru.wikipedia.org/wiki/%D0%92%D0%BD%D1%83%D0%BA%D0%BE%D0%B2%D0%BE_(%D0%B0%D1%8D%D1%80%D0%BE%D0%BF%D0%BE%D1%80%D1%82)'))
        bot.send_message(m.chat.id, "Выбери, что тебе интересно.", reply_markup=markup)

def portt(m):
    global helper
    helper = ''
    keyboard1 = types.ReplyKeyboardMarkup(True, True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
    msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputMonth)


def printMonth(m):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Январь', 'Февраль', 'Март']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Апрель', 'Май', 'Июнь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Июль', 'Август', 'Сентябрь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Октябрь', 'Ноябрь', 'Декабрь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in [' ', ' ', u"\U0001F519" + 'Назад']])
    msg = bot.send_message(m.chat.id, 'Выбери месяц отправления', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputMonth)


def inputMonth(m):
    if m.text ==u"\U0001F519" + 'Назад':
        printPort(m)
        return
    elif m.text == 'Домодедово' or 'Шереметьево' or 'Внуково':
        tariff(m)
    else:
        global month
        month = m.text
        inputDay(m)


def inputDay(m):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    k = 0
    for i in range(5):
        keyboard.row(str(k+1), str(k+2), str(k+3), str(k+4), str(k+5), str(k+6))
        k += 6
    keyboard.add(*[types.KeyboardButton(name) for name in ['31', u"\U0001F519" + "Назад"]])
    msg = bot.send_message(m.chat.id, 'Выбери день отправления', reply_markup=keyboard)
    bot.register_next_step_handler(msg, inputDirect)

def tariff(m):
    global port
    port = m.text
    keyboard1 = types.ReplyKeyboardMarkup(True, True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Эконом']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Комфорт']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Комфорт+']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Минивен']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Бизнес', u"\U0001F519" + 'Назад']])
    msg = bot.send_message(m.chat.id, 'Выбери тариф', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputTariff)

def inputTariff(m):
    if m.text == u"\U0001F519" + 'Назад':
        port(m)
        return
    else:
        global tarif
        tarif = m.text
        wishes(m)

def wishes(m):
    key = types.InlineKeyboardMarkup()
    key.add(types.InlineKeyboardButton(text='Кондиционер', callback_data="butt1"))
    key.add(types.InlineKeyboardButton(text='Некурящий водитель', callback_data="butt2"))
    key.add(types.InlineKeyboardButton(text='Перевозка велосипеда', callback_data="butt3"))
    key.add(types.InlineKeyboardButton(text='Детское кресло', callback_data="butt4"))
    key.add(types.InlineKeyboardButton(text='Перевозка животных', callback_data="butt5"))
    key.add(types.InlineKeyboardButton(text='Ожидание в пути', callback_data="butt6"))
    key.add(types.InlineKeyboardButton(text='Ничего не нужно', callback_data="butt7"))
    key.add(types.InlineKeyboardButton(text='Готово', callback_data="butt8"))

    bot.send_message(m.chat.id, 'Дополнительные пожелания', reply_markup=key)

    @bot.callback_query_handler(func=lambda call: True)
    def inline(call):
        global help1, help2, help3, help4, help5, help6
        if call.data == 'butt1':
            if help1 == '':
                help1 = '1'
                bot.send_message(m.chat.id, 'Вы выбрали кондиционер, хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help1 = ''
                bot.send_message(m.chat.id, 'Вы отменили выбор кондиционера, хотите выбрать что-то еще?')
        if call.data == 'butt2':
            if help2 == '':
                help2 = '1'
                bot.send_message(m.chat.id, 'Вы выбрали "Некурящий водитель", хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help2 = ''
                bot.send_message(m.chat.id, 'Вы отменили выбор "Некурящий водитель", хотите выбрать что-то еще?')
        if call.data == 'butt3':
            if help3 == '':
                help3 = '3'
                bot.send_message(m.chat.id, 'Вы выбрали "Перевозка велосипеда", хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help3 = ''
                bot.send_message(m.chat.id, 'Вы отменили "Перевозка велосипеда", хотите выбрать что-то еще?')
        if call.data == 'butt4':
            if help4 == '':
                help4 = '1'
                bot.send_message(m.chat.id, 'Вы выбрали "Детское кресло", хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help4 = ''
                bot.send_message(m.chat.id, 'Вы отменили "Детское кресло", хотите выбрать что-то еще?')
        if call.data == 'butt5':
            if help5 == '':
                help5 = '1'
                bot.send_message(m.chat.id, 'Вы выбрали "Перевозка животных", хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help5 = ''
                bot.send_message(m.chat.id, 'Вы отменили "Перевозка животных", хотите выбрать что-то еще?')
        if call.data == 'butt6':
            if help5 == '':
                help5 = '1'
                bot.send_message(m.chat.id, 'Вы выбрали "Ожидание в пути", хотите выбрать что-то еще? Чтобы отменить выбор, нажмите еще раз.')
            else:
                help5 = ''
                bot.send_message(m.chat.id, 'Вы отменили "Ожидание в пути", хотите выбрать что-то еще?')
        if call.data == 'butt7':
            help1 = ''
            help2 = ''
            help3 = ''
            help4 = ''
            help5 = ''
            help6 = ''
            taxiGeo(m)
        if call.data == 'butt8':
            taxiGeo(m)

def taxiGeo(m):
    keyboard1 = types.ReplyKeyboardMarkup(True, True)
    keyboard1.add(types.KeyboardButton(text="Отправить местоположение", request_location=True))
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Не отправлять']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in [u"\U0001F519" + 'Назад']])
    msg = bot.send_message(m.chat.id, 'Ваше местоположение...', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputGeo)

def inputGeo(m):
    if m.text != 'Не отправлять':
        bot.send_message(m.chat.id, type(m.location))
        loc=m.location
        searchAndCreateLinkTaxi(m,loc)
    elif m.text == 'Не отправлять':
        loc=''
        searchAndCreateLinkTaxi(m, loc)
        return
    elif m.text == u"\U0001F519" + 'Назад':
        tariff(m)

def searchAndCreateLinkTaxi(m,loc):
    if loc!='':
        userLon = loc.longitude
        userLan = loc.latitude

    classUser = tarif
    req = ""
    portTaxi = port

    #bot.send_message(m.chat.id, str(userLon) + ' ' + str(userLan))
    rll = ""
    classTaxi = ""

    portLon = ""
    portLan = ""

    if loc!='':
        rllUser = str(userLon) + "," + str(userLan)
    else:
        rllUser =''

    if portTaxi == "Домодедово":
        portLon = "37.897951"
        portLan = "55.416006"
    elif portTaxi == "Внуково":
        portLon = "37.2961100"
        portLan = "55.6119400"
    elif portTaxi == "Шереметьево":
        portLon = "38.4986800"
        portLan = "55.0091300"
    rll = portLon + "," + portLan

    if classUser == 'Эконом':
        classTaxi = "econom"
    elif classUser == 'Комфорт':
        classTaxi = "business"
    elif classUser == 'Комфорт+':
        classTaxi = "comfortplus"
    elif classUser == 'Минивен':
        classTaxi = "minivan"
    elif classUser == 'Бизнес':
        classTaxi = "vip"

    if (rllUser == ''):
        link = "https://taxi-routeinfo.taxi.yandex.net/taxi_info?rll=" + rll + "&clid=aerohelperbot&apikey=cb4b360f0b884277a7d15fe87ae9cd6e&class=" + classTaxi
    else:
        if userchange == "in":
            link = "https://taxi-routeinfo.taxi.yandex.net/taxi_info?rll=" + rllUser + "~" + rll + "&clid=aerohelperbot&apikey=cb4b360f0b884277a7d15fe87ae9cd6e&class=" + classTaxi
        else:
            link = "https://taxi-routeinfo.taxi.yandex.net/taxi_info?rll=" + rll + "~" + rllUser + "&clid=aerohelperbot&apikey=cb4b360f0b884277a7d15fe87ae9cd6e&class=" + classTaxi

    response = requests.get(link)  # отправляем запрос на получение кода страницы

    response.raise_for_status()
    d = response.json()  # do not create the result file until json is parsed

    options = d['options']
    if rllUser != '':
        distance = d['distance']
        waiting_time = str(options[0]['waiting_time'])
        time = str(d['time_text'])
    classCode = str(options[0]['class_level'])
    price = str(options[0]['price'])


    bot.send_message(m.chat.id, price+' '+classCode)
    options = d['options']
    classCode = str(options[0]['class_level'])

#    if userchange == "in":
#        linkUser = "https://3.redirect.appmetrica.yandex.com/route?start-lat=" + userLan + "&start-lon=" + userLon + "&end-lat=" + portLan + "&end-lon=" + portLon + "&level=" + classCode + "&ref=aerohelperbot&appmetrica_tracking_id=1178268795219780156"
 #   else:
 #       linkUser = "https://3.redirect.appmetrica.yandex.com/route?start-lat=" + portLan + "&start-lon=" + portLon + "&end-lat=" + userLan + "&end-lon=" + userLon + "&level=" + classCode + "&ref=aerohelperbot&appmetrica_tracking_id=1178268795219780156"


def inputDirect(m):
    if m.text == u"\U0001F519" + 'Назад':
        printMonth(m)
        return


    else:
        global day
        day = m.text
        msg = bot.send_message(m.chat.id, 'Введите направление')
        bot.register_next_step_handler(msg, printAnsSearch)


def printAnsSearch(m):
    global direct
    direct = m.text
    bot.send_message(m.chat.id, u"\U0001F50E"+" В поисках данных...")
    try: getTime(port, day, month, direct)
    except:
        bot.send_message(m.chat.id, 'Ничего не найдено, давайте попробуем еще раз?')
        start(m)

    for i in range(len(timeP)):
        #Проверка наличия данных о платформе и терминале
        if str(plat[i]) == '' and str(term[i]) == 'None':
            ourAns =u'\U0001F30D'+'Направление: '+rightAns+'\n'+u'\U0001F558' +'Время отправления: '+timeP[i][11:16] + '\n'+ u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n'+u'\u2708' +'Модель самолета: '+ mod[i] + '\n'+u'\U0001F3E2'+'Компания: ' + comp[i]
            bot.send_message(m.chat.id, ourAns)
        elif str(plat[i]) != '' and str(term[i]) == 'None':
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n'  + 'Платформа: ' + plat[i]
            bot.send_message(m.chat.id, ourAns)
        elif str(plat[i]) == '' and str(term[i]) != 'None':
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n' + u"\U0001F6AA" + 'Терминал: ' + str(term[i])
            bot.send_message(m.chat.id, ourAns)
        else:
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n' + 'Платформа: ' + plat[i] + '\n' + u"\U0001F3E2" + 'Терминал: ' + str(term[i])
            bot.send_message(m.chat.id, ourAns)
    endmenu(m)

def getTime(port, day, month, direct):
    # Небольшая обработка для запроса
    if (len(day) == 1):
        day = "0" + day

    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь''Октябрь', 'Ноябрь',
              'Декабрь']
    for i in range(len(months)):
        if (month == months[i]):
            month = str(i + 1)
            break
    if (len(month) == 1):
        month = "0" + month

    if (len(port) != 3):
        ports = {'Домодедово': 'DME', 'Шереметьево': 'SVO', 'Внуково': 'VKO'}
        port = ports[port]

    link = "https://api.rasp.yandex.net/v3.0/schedule/?apikey=94b5c4bf-9350-4f45-896d-ad5e244bc10e&system=iata&date=2020-" + month + "-" + day + "&transport_types=plane&station=" + port

    response = requests.get(link)  # отправляем запрос на получение кода страницы

    response.raise_for_status()
    d = response.json()  # do not create the result file until json is parsed

    schedule = pd.DataFrame(d['schedule'])

    departure = schedule.departure
    terminal = schedule.terminal
    platform = schedule.platform
    threads = schedule.thread
    direction = {'': 0}

    for i in range(len(threads)):
        dirt = threads[i].get('title')
        dirt = dirt[9::]
        direction[dirt] = 0

    del direction['']

    for i in range(len(threads)):
        dirt = threads[i].get('title')
        dirt = dirt[9::]
        direction[dirt] = 0
    ans = direct
    for i in range(len(ans)):
        for k, v in direction.items():
            if ((i < len(k)) and (ans[i] == k[i])):
                direction[k] = direction[k] + 1
    direction_list = sorted(direction.items(), key=lambda kv: kv[1])
    max_value = max(x[1] for x in direction_list)
    ans1 = [x for x in direction_list if x[1] == max_value]
    global rightAns
    rightAns = ans1[0][0]

    rightAns = 'Москва — ' + rightAns
    flight = []

    global timeP, number_Flight, term, plat, mod, comp
    timeP = []
    number_Flight = []
    term = []
    plat = []
    mod = []
    comp = []

    for i in range(len(threads)):
        if (rightAns == threads[i].get('title')):
            flight.append(i)

    for i in flight:
        timeP.append(departure[i])
        number_Flight.append(threads[i].get('number'))
        term.append(terminal[i])
        plat.append(platform[i])
        mod.append(threads[i].get('vehicle'))
        comp.append(threads[i].get('carrier').get('title'))

def endmenu(m):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    button_1 = types.KeyboardButton(text=u"\U0001F3E1" + "Главное меню")
    button_2 = types.KeyboardButton(text=u"\U0001F519" + "Назад")
    keyboard.row(button_1, button_2)
    msg = bot.send_message(m.chat.id, 'Список рейсов получен.', reply_markup=keyboard)
    bot.register_next_step_handler(msg, realiseEndmenu)

def realiseEndmenu(m):
    if m.text == u"\U0001F3E1" + 'Главное меню':
        start(m)
    else:
        inputDay(m)




bot.polling()
