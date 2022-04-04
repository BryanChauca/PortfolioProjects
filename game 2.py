#building a guessing game
import random

def play():
    welcome_message = "Welcome you have 5 tries to get it right.(1-10)"
    print(welcome_message)
    print('-' * 50)
    number = random.randint(1, 10)
    tries_remaining = 3

    while tries_remaining > 0:
        guess = int(input("What would be your guess? \n"))
        if guess == number:
            print("Congrats you win!!")
            break
        else:
            tries_remaining -= 1
            print(f"Incorrect. Try again, you have {tries_remaining} tries left")

    if tries_remaining == 0:
        print(f"Game over, the winning number was {number}")

    play_again = input("would you like to play again? type (y/n) \n")
    if play_again == 'y':
        return play()
    elif play_again == 'n':
        print("See you soon!")

    return play

play()
