import re

# Get the answer.
answer = "What's Up, Doc?"

answer = answer.upper()

# Pre-Game Setup.
answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else: 
        answer_guessed.append(True)

# Logic of the game.
num_of_incorrect_guesses = 5

current_incorrect_guesses = 0

letters_guessed = []

# user gameplay Logic.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Display game summary.
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")