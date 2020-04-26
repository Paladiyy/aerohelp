import telebot
from telebot import types
bot = telebot.TeleBot('1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0')
var = ""
var1 = ""
var2 = ""
var4 = ""

@bot.message_handler(content_types=['text'])
def names(m):
    if m.text == u"\u2708" + 'Информация о рейсе' or m.text == u"\U0001F4BB" + 'Разработчики':
        name(m)
    else:
        start(m)

@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, "Привет, я Aerohelper. Давай посмотрим список доступных команд.")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [u"\u2708" + 'Информация о рейсе', u"\U0001F4BB" + 'Разработчики']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == u"\U0001F4BB" + 'Разработчики':
        namem(m)
    else:
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, name2)

def namem(m):
    smile = u'\U0001F525'
    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
    msg = bot.send_message(m.chat.id, smile + 'by egorov dynasty', reply_markup=keyboard1)
    bot.register_next_step_handler(msg, name2)

def name2(m):
    if m.text == 'Назад':
        start(m)
        return
    else:
        global var
        var = m.text
        name3(m)

def name3(m):
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Январь','Февраль','Март']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Апрель','Май','Июнь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Июль','Август','Сентябрь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Октябрь','Ноябрь','Декабрь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in [' ',' ','Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери месяц отправления', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, name4)

def name4(m):
    if m.text == 'Назад':
        name(m)
        return
    else:
        global var1
        var1 = m.text
        name5(m)

def name5(m):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    button_date1= types.KeyboardButton(text="1")
    button_date2= types.KeyboardButton(text="2")
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
    bot.register_next_step_handler(msg, name6)

def name6(m):
    if m.text == 'Назад':
        name3(m)
        return
    else:
        global var2
        var2 = m.text
        msg = bot.send_message(m.chat.id, 'Введите направление')
        bot.register_next_step_handler(msg, name7)

def name7(m):
    global var4
    var4 == m.text



bot.polling()