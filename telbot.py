import telebot

bot = telebot.TeleBot('5012011658:AAEAEfgFnYgtejCXC-qqKMk5IJF3XthNDEQ')


@bot.message_handler(commands=['start'])
def start(message):
    ans=message.from_user.first_name
    bot.send_message(message.chat.id, 'Пошел нахуй ' + ans, parse_mode='html')
    bot.send_message(message.chat.id, "-)")

@bot.message_handler()
def get_user_taxt(message):
    if message.text =='/photo':
        photo=open('gachi.gif','rb')

        bot.send_photo(message.chat.id, photo)





bot.polling(none_stop=True)
