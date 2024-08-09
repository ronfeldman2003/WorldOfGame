import GuessGame
import MemoryGame
import CurrencyRouletteGame


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    def choose(choose_type, range_from, range_to):
        choice = 0
        while not (range_from <= choice <= range_to):
            try:
                if choose_type == "number":
                    choice = int(input(f"Enter the game number:"))
                elif choose_type == "difficulty":
                    choice = int(input("Please choose game difficulty from 1 to 5:"))

                if not (range_from <= choice <= range_to):
                    print("The number you choose is not an option lets try again")
            except ValueError as e:
                error_message = str(e)
                invalid_literal = error_message.split("'")[1]
                print(f"'{invalid_literal}' is not a game {choose_type} from the options. it's not even a number lets try again")
        return choice
    game_number = choose("number", 1, 3)
    game_difficulty = choose("difficulty", 1, 5)

    def start_game(game_num,game_diff):
        match game_num:
            case 1:
                return MemoryGame.play(game_diff)
            case 2:
                return GuessGame.play(game_diff)
            case 3:
                return CurrencyRouletteGame.play(game_diff)
    start_game(game_number, game_difficulty)