import word_utils

allowed_answers = word_utils.load_answers()
allowed_guesses = word_utils.load_allowed_words() + allowed_answers

print("This is an aid to narrow down possibilities for wordle.")

user_input = ""
remaining_guesses = list(allowed_guesses)

while user_input != '0':
    print("Enter the word you chose or 0 to exit.")
    user_input = input().lower()
    if user_input in allowed_answers or user_input in remaining_guesses:
        print("Enter the result of the word")
        print("(i.e. 0 0 1 0 2, 1 means correct letter and 2 means correct letter and position)")
        input_result = input()
        result_as_int = []
        for value in input_result.split(" "):
            result_as_int.append(int(value))
        print(f"Input {user_input} resulted in {result_as_int}.")
        remaining_guesses = word_utils.filter_guesses(user_input, result_as_int, remaining_guesses)
        if len(remaining_guesses) > 50:
            print(f"The first 50 of the remaining {len(remaining_guesses)} guesses are {remaining_guesses[:50]}")
        else:
            print(f"The remaining guesses are {remaining_guesses}")
    elif user_input != '0':
        print(f"Sorry, it doesn't look like {user_input} is an allowed word.")

