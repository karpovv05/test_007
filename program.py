import telebot

bot = telebot.TeleBot('5012011658:AAEAEfgFnYgtejCXC-qqKMk5IJF3XthNDEQ')


@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'Пошел нахуй', parse_mode='html')


bot.polling(none_stop=True)
