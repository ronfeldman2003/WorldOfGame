import random
difficulty = 5
secret_number = 0


def generate_number():
    global secret_number
    secret_number = random.randint(1,difficulty)
    print(secret_number)


def get_guess_from_user():
    while True:
        try:
            return int(input(f"Guess a number between 1 and {difficulty}:"))
        except ValueError as e:
            error_message = str(e)
            invalid_literal = error_message.split("'")[1]
            print(f"'{invalid_literal}' is not a number, try again")


def compare_results(guess):
    return guess == secret_number


def play(game_difficulty):
    global difficulty
    difficulty = game_difficulty
    print("Welcome to the guess game!")
    generate_number()
    return compare_results(get_guess_from_user())

