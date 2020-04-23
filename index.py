import telebot
bot = telebot.TeleBot('1210073832:AAE9sKHHH6ZPm581AhDbKfhKUYM7qNWmhc0')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я Aerohelper. Давай посмотрим список доступных команд: Null')
bot.polling()