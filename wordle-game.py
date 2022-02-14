import random
import word_utils
import sys

allowed_answers = word_utils.load_answers()
allowed_guesses = word_utils.load_allowed_words() + allowed_answers

unused_letters = []

unicode = 97
while unicode < 123:
    unused_letters.append(chr(unicode))
    unicode += 1

random_index = random.randrange(len(allowed_answers))
chosen_answer = allowed_answers[random_index]
guess_random_index = random.randrange(len(allowed_guesses))
guess = allowed_guesses[guess_random_index]
#print(f"The chosen answer is {chosen_answer} ({random_index})")
#print(f"Testing diff on answer and guess {guess}: {word_utils.get_diff(guess, chosen_answer)}")
print("This is a wordle practice program. The game is based on the NY Times online game.\nTry to guess the five-letter word!")
previous_guesses = ["_ _ _ _ _"]
user_guess = ""
num_guesses = 0
while not word_utils.match(user_guess, chosen_answer) and num_guesses < 6:
    for attempt in previous_guesses:
        print(attempt)
    print(f"You have not used these letters: {unused_letters}")
    user_guess = input().lower()
    if user_guess in allowed_guesses or user_guess in allowed_answers:
        num_guesses += 1
        word_utils.update_result(user_guess, chosen_answer, previous_guesses, unused_letters)
    else:
        print(f"Sorry, {user_guess} is not an allowed guess.")
        user_guess = ""
if word_utils.match(user_guess, chosen_answer):
    print(f"Nice! you got it! the word was {chosen_answer}")    
    print(f"\nIt took you {num_guesses} guesses.")
else:
    print(f"Sorry, you took too many tries.\nThe answer was {chosen_answer}")


