import word_utils


allowed_guesses = word_utils.load_answers() + word_utils.load_allowed_words()

print("Getting info for the first 100 words as guesses")
patterns = word_utils.enumerate_patterns()
guess_info = []
guesses = {}
num_finished = 0
for guess in allowed_guesses:
    print(f"Getting info for the word {guess}")
    pattern_matches = word_utils.get_info_2(guess, patterns, allowed_guesses)
    print(f"matches for {guess}:")
    total_expected_information = 0
    num_allowed_guesses = len(allowed_guesses)
    for i in range(len(pattern_matches)):
        #print(f"{word_utils.pad_to_5(word_utils.convert_to_base_3(i))}: {pattern_matches[i]}")
        if pattern_matches[i] > 0:
            probability = pattern_matches[i]/num_allowed_guesses
            total_expected_information += probability * word_utils.info_from_probability(probability)
    print(f"Total expected information for {guess}: {total_expected_information}")



#for guess in allowed_guesses:
#    average_info = word_utils.get_info(guess, patterns, allowed_guesses)
#    #print(f"Average filtered down for {guess} was {average_info}")
#    guess_info.append(average_info)
#    guesses[average_info] = guess
#    if num_finished % 100 == 0:
#        print(f"{num_finished} out of {len(allowed_guesses)} finished.")
#    num_finished += 1
#
#best = min(guess_info)
#print(f"Best guess was {guesses[best]}, with an average of {best}")
#info_results = open("info-results.txt")
#for info in guesses:
#    info_results.write(f"{guesses[info]}, info,")
#info_results.close()



