import os

SCORES_FILE_NAME = "/tmp/Scores.txt"
BAD_RETURN_CODE = "1"


def screen_cleaner():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux/Mac
        os.system('clear')

