import os

SCORES_FILE_NAME = "/app/Scores12.txt"
BAD_RETURN_CODE = "1"


def screen_cleaner():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

