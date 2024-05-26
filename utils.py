import os, art

def clear_screen():
    """Clear the console screen"""

    return os.system('cls||clear')

# Number of turns for any level selected by the user
EASY_LEVEL = 10
HARD_LEVEL = 5

def guess_number(in_difficulty, in_answer):
    """Function to guess the number randomly created, based on the difficulty chosen by the user"""

    game_over = False
    vicotory = False

    if in_difficulty == "easy":
        num_tries = EASY_LEVEL
    
    else:
        num_tries = HARD_LEVEL

    clear_screen()

    while num_tries > 0 and not game_over:
        print(f"You have {num_tries} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        if user_guess < in_answer:
            clear_screen()
            print(f"{art.too_low}\n")
            print("Guess again.")
            num_tries -= 1

        elif user_guess > in_answer:
            clear_screen()
            print(f"{art.too_high}\n")
            print("Guess again.")
            num_tries -= 1

        else:
            clear_screen()
            game_over = True
            vicotory = True
              
    if vicotory:
        # EASTER EGG
        if in_answer == 69:
                print(f"{art.easter_egg}\n")

        else:
            print(f"{art.victory}\n")

        print(f"Congratulations! You've won the game with {num_tries} remaining attempt(s).")
        print(f"The answer is {in_answer}.")

    else:
        clear_screen()
        print(f"{art.defeat}\n")
        print("You've ran out of attempts, you lose.")
        print(f"The answer is {in_answer}.")