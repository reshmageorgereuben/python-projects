import random

guess_number = random.randint(1,100)

while True:
    user_input = input("Guess number between 1 and 100:")
    try:
        num = int(user_input)
        if num > guess_number:
            print("Too High!")
        elif num < guess_number:
            print("Too Low!")
        elif num == guess_number:
            print("Congrats!! Guessed the correct number.")
            break

    
    except ValueError:
        print("Please enter a valid number")
    

