import telebot
from telebot import types

import configuration.config as cfg
from item import Item
from parsers.technopark_parser import TechnoparkParser
from parsers.mvideo_parser import MvideoParser


bot = telebot.TeleBot(cfg.TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message) -> None:
    markup = keyboard_markup()

    bot.send_message(message.chat.id, cfg.WELCOME_MSG, reply_markup=markup)
    bot.register_next_step_handler(message, handle_message)


def keyboard_markup() -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup()

    tp_button = types.KeyboardButton(cfg.TECHNOPARK_BTN)
    mv_button = types.KeyboardButton(cfg.MVIDEO_BTN)
    log_button = types.KeyboardButton(cfg.SEARCHLOG_BTN)

    markup.add(tp_button, mv_button, log_button)
    
    return markup


def handle_message(message) -> None:
    match message.text:  

        case 'Technopark':  
            message = bot.send_message(message.chat.id, cfg.REQUEST_QUESTION, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, technopark_script)

        case 'Mvideo':
            message = bot.send_message(message.chat.id, cfg.REQUEST_QUESTION, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message, mvideo_script)

        case 'Search log':
            bot.send_message(message.chat.id, reply_markup=types.ReplyKeyboardRemove())
            bot.register_next_step_handler(message)  #log_script


def technopark_script(message):
    products = TechnoparkParser()
    products = products.scraping(message.text)

    bot.send_message(message.chat.id, products)

    send_welcome(message, cfg.REPEAT_MESSAGE)


def mvideo_script(message):
    products = MvideoParser()
    products = products.scraping(message.text)

    picture = products[0].pic_url

    bot.send_photo(message.chat.id, photo=picture, caption=products)

    send_welcome(message, cfg.REPEAT_MESSAGE)

# def log_script(message):
#     return


if __name__ == '__main__':
    bot.infinity_polling()