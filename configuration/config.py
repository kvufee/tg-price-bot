import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get('TOKEN')

WELCOME_MSG = 'Greetings'
TECHNOPARK_BTN = 'Technopark'
SEARCHLOG_BTN = 'Search log'
REQUEST_QUESTION = 'What are you looking for?'

SLEEP_DURATION = 5
