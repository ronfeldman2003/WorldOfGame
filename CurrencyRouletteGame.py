import requests
import random

difficulty = 5


def get_money_interval(money_usd):
    url = "https://v6.exchangerate-api.com/v6/ee81e503ad1bf1c0777ab7be/latest/USD"
    response = requests.get(url)
    conversion_rate = response.json().get("conversion_rates").get("ILS")
    money_ils = money_usd*conversion_rate
    money_ils = round(money_ils, 2)
    interval = [(money_ils-(5-difficulty)), (money_ils+(5-difficulty))]
    return interval


def get_guess_from_user(money_usd):
    while True:
        try:
            return float(input(f"guess how much ILS is {money_usd} USD:"))
        except ValueError as e:
            error_message = str(e)
            invalid_literal = error_message.split("'")[1]
            print(f"'{invalid_literal}' is not a number, try again")


def play(game_difficulty):
    print("welcome to currency roulette game!")
    global difficulty
    difficulty = game_difficulty
    usd_random = random.randint(1, 100)
    interval = get_money_interval(usd_random)
    guess = get_guess_from_user(usd_random)
    return interval[0] <= guess <= interval[1]

