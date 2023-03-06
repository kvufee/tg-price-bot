import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get('TOKEN')

WELCOME_MSG = 'Greetings'
TECHNOPARK_BTN = 'Technopark'
MVIDEO_BTN = 'Mvideo'
SEARCHLOG_BTN = 'Search log'
REQUEST_QUESTION = 'What are you looking for?'

SLEEP_DURATION = 5

REPEAT_MESSAGE = 'Wanna find something else?'
