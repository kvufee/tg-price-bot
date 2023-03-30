import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get('TOKEN')

WELCOME_MSG = 'Greetings'
ELDORADO_BTN = 'Eldorado'
MVIDEO_BTN = 'Mvideo'
SEARCHLOG_BTN = 'Search log'
REQUEST_QUESTION = 'What are you looking for?'

SLEEP_DURATION = 3
INPUT_DURATION = 1

REPEAT_MESSAGE = 'Wanna find something else?'
