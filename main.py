import telebot

bot = telebot.TeleBot('7483627073:AAE0PN-TscROJLj7dqYRDOct_5b3wKBeW6g')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')



bot.polling(none_stop=True)