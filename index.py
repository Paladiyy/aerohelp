import telebot
from telebot import types
bot = telebot.TeleBot('1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0')
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*[types.KeyboardButton(name) for name in ['Информация о рейсе', 'Разработчики']])
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
        msg = bot.send_message(m.chat.id, 	smile + 'by egorov dynasty', reply_markup=keyboard1)
        bot.register_next_step_handler(msg, name2)
def name2(m):
    if m.text == 'Назад':
        start(m)
        return


        
bot.polling()