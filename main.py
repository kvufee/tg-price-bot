import telebot

from telebot import types

from configuration.config import TOKEN
from parsers.technopark_parser import TechnoparkParser


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message) -> None:
    markup = keyboard_markup()

    bot.send_message(message.chat.id, 'Greetings🤨', reply_markup=markup)
    bot.register_next_step_handler(message, handle_message)


def keyboard_markup() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup()

    tp_button = types.KeyboardButton('Technopark')
    log_button = types.KeyboardButton('Search log')

    markup.add(tp_button, log_button)

    return markup


def handle_message(message):
    match message.text:  

        case 'Technopark':
            message = bot.send_message(message.chat.id, 'What do you want to find?', reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, technopark_script)

        case 'Search log':
            bot.send_message(message.chat.id, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, log_script)


def technopark_script(message):
    product_list = TechnoparkParser.item_list(product_name=message.text)


    return product_list

def log_script(message):


    return




bot.infinity_polling()