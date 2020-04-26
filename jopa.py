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


TOKEN = "1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def calendar_handler(bot,update):
    update.message.reply_text("Please select a date: ", reply_markup=telegramcalendar.create_calendar())


def inline_handler(bot,update):
    selected,date = telegramcalendar.process_calendar_selection(bot, update)
    if selected:
        bot.send_message(chat_id=update.callback_query.from_user.id, text="You selected %s" % (date.strftime("%d/%m/%Y")), reply_markup=ReplyKeyboardRemove())



up = Updater("1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0", use_context=True)

up.dispatcher.add_handler(CommandHandler("calendar",calendar_handler))
up.dispatcher.add_handler(CallbackQueryHandler(inline_handler))

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
        var = m.text
        name3(m, var)
        return var
def name3(m, var):
        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Январь','Февраль','Март']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Апрель','Май','Июнь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Июль','Август','Сентябрь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in ['Октябрь','Ноябрь','Декабрь']])
        keyboard1.add(*[types.KeyboardButton(advert) for advert in [' ',' ','Назад']])
        msg = bot.send_message(m.chat.id, 'Выбери месяц отправления', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, name4(m,var))

def name4(m, arg):


    if m.text == 'Назад':
        name(m)
        return
    else:
        bot.send_message(m.chat.id, 'Аэропорт:' + arg + 'Месяц:' + m.text)








bot.polling()