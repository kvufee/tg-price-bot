import telebot

from telebot import types


token = '5727630538:AAEbDBQ-o18UH6ol8FZAyaRzg9tH2DgXFqo'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Greetings🤨')

@bot.message_handler(commands=['button'])
def option_button(message):
    markup = types.ReplyKeyboardMarkup(row_width = 2)
    itembtn1 = types.KeyboardButton('Search')
    itembtn2 = types.KeyboardButton('Log')
    itembtn3 = types.KeyboardButton('Favourite')
    itembtn4 = types.KeyboardButton('About')

    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

markup = types.ReplyKeyboardRemove(selective=False)
bot.send_message(chat_id, "How can I help you?", reply_markup=markup)


bot.infinity_polling()