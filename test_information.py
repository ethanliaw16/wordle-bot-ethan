import word_utils

allowed_guesses = word_utils.load_answers() + word_utils.load_allowed_words()

print("Getting info for the first 100 words as guesses")
patterns = word_utils.enumerate_patterns()
guess_info = []
guesses = {}
num_finished = 0
for guess in allowed_guesses:
    average_info = word_utils.get_info(guess, patterns, allowed_guesses)
    #print(f"Average filtered down for {guess} was {average_info}")
    guess_info.append(average_info)
    guesses[average_info] = guess
    if num_finished % 100 == 0:
        print(f"{num_finished} out of {len(allowed_guesses)} finished.")
    num_finished += 1

best = min(guess_info)
print(f"Best guess was {guesses[best]}, with an average of {best}")
info_results = open("info-results.txt")
for info in guesses:
    info_results.write(f"{guesses[info]}, info,")
info_results.close()



