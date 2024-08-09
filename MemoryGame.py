import random
from time import sleep
import sys
difficulty = 1


def generate_sequence():
    numbers_list = []
    for i in range(difficulty):
        numbers_list.append(random.randint(1, 101))
    return numbers_list


def get_list_from_user():
    user_guess_list = []
    for i in range(difficulty):
        while len(user_guess_list) != i+1:
            try:
                user_guess_list.append(int(input(f"what was the {i+1} number:")))
            except ValueError as e:
                error_message = str(e)
                invalid_literal = error_message.split("'")[1]
                print(f"'{invalid_literal}' is not a number, try again")
    return user_guess_list


def is_list_equal(list1, list2):
    return list1 == list2


def play(game_difficulty):
    print("welcome to memory game number will show in 5 seconds")
    global difficulty
    difficulty = game_difficulty
    numbers = generate_sequence()
    sleep(5)
    sys.stdout.write(','.join(str(number) for number in numbers))
    sleep(0.7)
    sys.stdout.write('\r'+"*************\n")
    sys.stdout.flush()
    user_guess = get_list_from_user()
    return is_list_equal(numbers, user_guess)
