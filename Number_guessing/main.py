from random import randint
from art import logo

EASY_LEVEL_LIFE = 10
HARD_LEVEL_LIFE = 5


def set_difficulty():
    select_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if select_level == "easy":
        return EASY_LEVEL_LIFE
    elif select_level == "hard":
        return HARD_LEVEL_LIFE


def check_answer(guess, answer, life):
    if guess > answer:
        print("Too high.")
        return life - 1
    elif guess < answer:
        print("Too low.")
        return life - 1
    else:
        print(f"You got it! The answer was {answer}")


def play_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    computer_pick = randint(1, 100)

    life = set_difficulty()

    user_pick = -1

    while user_pick != computer_pick:
        print(f"You have {life} attempts remaining to guess the number.")
        user_pick = int(input("Make a guess: "))

        life = check_answer(user_pick, computer_pick, life)

        if life == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {computer_pick}")
            return
        elif user_pick != computer_pick:
            print("Guess again")


play_game()
