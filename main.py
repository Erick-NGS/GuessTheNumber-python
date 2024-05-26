import art, random, utils

num_answer = random.randint(1, 100)


print(art.welcome)
print("Welcome to the 'Guessing Number Game'!")
print("The goal is to guess a random number between 1 & 100. Good luck and may the force be with you!")
# Answer
# print(f"The answer is {num_answer}")
game_question = input("Select a difficulty. Type 'easy' or 'hard': ")


if game_question == "easy":
    # Easy (10 tries)
    utils.guess_number("easy", num_answer)
elif game_question == "hard":
    # Hard (5 tries)
    utils.guess_number("hard", num_answer)
else:
    print("Option typed not recognized, please restart the game!")