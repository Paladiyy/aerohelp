import telebot
from telebot import types
import requests
import pandas as pd

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

#@bot.message_handler(content_types=['text'])
#def names(m):
 #   if m.text == u"\u2708" + 'Информация о рейсе' or m.text == u"\U0001F4BB" + 'Разработчики':
   #     name(m)
  #  else:
   #     start(m)


@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, "Привет, я Aerohelper. Давай посмотрим список доступных команд.")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        *[types.KeyboardButton(name) for name in [u"\u2708" + 'Информация о рейсе', u"\U0001F4BB" + 'Разработчики']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, printPort)


def printPort(m):
    if m.text == u"\U0001F4BB" + 'Разработчики':
        printDev(m)
    else:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, inputPort)


def printDev(m):
    smile = u'\U0001F525'
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
    msg = bot.send_message(m.chat.id, smile + 'by egorov dynasty', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputPort)


def inputPort(m):
    if m.text == 'Назад':
        start(m)
        return
    else:
        global port
        port = m.text
        printMonth(m)


def printMonth(m):
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Январь', 'Февраль', 'Март']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Апрель', 'Май', 'Июнь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Июль', 'Август', 'Сентябрь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Октябрь', 'Ноябрь', 'Декабрь']])
    keyboard1.add(*[types.KeyboardButton(advert) for advert in [' ', ' ', 'Назад']])
    msg = bot.send_message(m.chat.id, 'Выбери месяц отправления', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, inputMonth)


def inputMonth(m):
    if m.text == 'Назад':
        printPort(m)
        return
    else:
        global month
        month = m.text
        inputDay(m)


def inputDay(m):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    button_date1 = types.KeyboardButton(text="1")
    button_date2 = types.KeyboardButton(text="2")
    button_date3 = types.KeyboardButton(text="3")
    button_date4 = types.KeyboardButton(text="4")
    button_date5 = types.KeyboardButton(text="5")
    button_date6 = types.KeyboardButton(text="6")
    keyboard.row(button_date1, button_date2, button_date3, button_date4, button_date5, button_date6)
    button_date7 = types.KeyboardButton(text="7")
    button_date8 = types.KeyboardButton(text="8")
    button_date9 = types.KeyboardButton(text="9")
    button_date10 = types.KeyboardButton(text="10")
    button_date11 = types.KeyboardButton(text="11")
    button_date12 = types.KeyboardButton(text="12")
    keyboard.row(button_date7, button_date8, button_date9, button_date10, button_date11, button_date12)
    button_date13 = types.KeyboardButton(text="13")
    button_date14 = types.KeyboardButton(text="14")
    button_date15 = types.KeyboardButton(text="15")
    button_date16 = types.KeyboardButton(text="16")
    button_date17 = types.KeyboardButton(text="17")
    button_date18 = types.KeyboardButton(text="18")
    keyboard.row(button_date13, button_date14, button_date15, button_date16, button_date17, button_date18)
    button_date19 = types.KeyboardButton(text="19")
    button_date20 = types.KeyboardButton(text="20")
    button_date21 = types.KeyboardButton(text="21")
    button_date22 = types.KeyboardButton(text="22")
    button_date23 = types.KeyboardButton(text="23")
    button_date24 = types.KeyboardButton(text="24")
    keyboard.row(button_date19, button_date20, button_date21, button_date22, button_date23, button_date24)
    button_date25 = types.KeyboardButton(text="25")
    button_date26 = types.KeyboardButton(text="26")
    button_date27 = types.KeyboardButton(text="27")
    button_date28 = types.KeyboardButton(text="28")
    button_date29 = types.KeyboardButton(text="29")
    button_date30 = types.KeyboardButton(text="30")
    keyboard.row(button_date25, button_date26, button_date27, button_date28, button_date29, button_date30)
    button_date31 = types.KeyboardButton(text="31")
    button_date32 = types.KeyboardButton(text=" ")
    button_date33 = types.KeyboardButton(text=" ")
    button_date34 = types.KeyboardButton(text=" ")
    button_date36 = types.KeyboardButton(text="Назад")
    keyboard.row(button_date31, button_date32, button_date33, button_date34, button_date36)
    msg = bot.send_message(m.chat.id, 'Выбери день отправления', reply_markup=keyboard)
    bot.register_next_step_handler(msg, inputDirect)


def inputDirect(m):
    if m.text == 'Назад':
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
            msg = bot.send_message(m.chat.id, ourAns)
            bot.register_next_step_handler(msg, start)
        elif str(plat[i]) != '' and str(term[i]) == 'None':
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n'  + 'Платформа: ' + plat[i]
            msg = bot.send_message(m.chat.id, ourAns)
            bot.register_next_step_handler(msg, start)
        elif str(plat[i]) == '' and str(term[i]) != 'None':
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n' + u"\U0001F6AA" + 'Терминал: ' + str(term[i])
            msg = bot.send_message(m.chat.id, ourAns)
            bot.register_next_step_handler(msg, start)
        else:
            ourAns = u'\U0001F30D' + 'Направление: ' + rightAns + '\n' + u'\U0001F558' + 'Время отправления: ' + timeP[i][11:16] + '\n' + u"\U0001F310" + 'Номер рейса: ' + number_Flight[i] + '\n' + u'\u2708' + 'Модель самолета: ' + mod[i] + '\n' + u'\U0001F3E2' + 'Компания: ' + comp[i] + '\n' + 'Платформа: ' + plat[i] + '\n' + u"\U0001F3E2" + 'Терминал: ' + str(term[i])
            msg = bot.send_message(m.chat.id, ourAns)
            bot.register_next_step_handler(msg, start)


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






bot.polling()