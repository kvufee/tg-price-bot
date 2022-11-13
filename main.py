import telebot

from configuration.config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message) -> None:
    
    bot.send_message(message.chat.id, 'Greetings🤨')


bot.infinity_polling()