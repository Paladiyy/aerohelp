import telebot
import telegramcalendar
import time
from telebot import types
import logging
from telegram.ext import Updater
from telegram.ext import  CallbackQueryHandler
from telegram.ext import  CommandHandler
from telegram import  ReplyKeyboardRemove
bot = telebot.TeleBot('1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о рейсе', 'Разработчики']])


var = ""
var1 = ""
var2 = ""

@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, "Привет, я Aerohelper. Давай посмотрим список доступных команд.")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о рейсе', 'Разработчики']])
    bot.send_message(m.chat.id, 'Выберите в меню что вам интересно!', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)



def name(m):
    if m.text == 'Информация о рейсе':
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Домодедово']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Шереметьево']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Внуково']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери аэропорт', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, name2)
    elif m.text == 'Разработчики':
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

@bot.message_handler(content_types=['text'])
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
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
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
    button_date35 = types.KeyboardButton(text=" ")
    button_date36 = types.KeyboardButton(text="Назад")
    keyboard.row(button_date31, button_date32, button_date33, button_date34, button_date35, button_date36)
    msg = bot.send_message(m.chat.id, 'Выбери месяц отправления', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name6)
def name6(m):

    if m.text == 'Назад':
        name3(m)
        return
    else:
        global var2
        var2 = m.text
        bot.send_message(m.chat.id, 'Аэропорт: ' + var + ', Месяц: ' + var1 + ', День: ' + var2)













bot.polling()