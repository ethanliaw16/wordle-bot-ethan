def load_answers():
    answers_file = open('allowed-answers.txt')
    return answers_file.read().split("\n")

def load_allowed_words():
    guesses_file = open('allowed-guesses.txt')
    return guesses_file.read().split("\n")


def match(word1, word2):
    return sum(get_diff(word1, word2)) == 10

def get_diff(guess, answer):
    result = [0] * 5
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result[i] = 2
        elif guess[i] in answer:
            result[i] = 1            
    return result

def update_result(user_guess, chosen_answer, previous_guesses, unused_letters):
    new_attempt = ""
    for i in range(len(user_guess)):
        if user_guess[i] in unused_letters:
            unused_letters.remove(user_guess[i])
        new_attempt += user_guess[i] + " "
    previous_guesses.append(new_attempt)
    new_attempt_diff = ""
    current_diff = get_diff(user_guess, chosen_answer)
    for i in current_diff:
        new_attempt_diff += str(i) + " "
    previous_guesses.append(new_attempt_diff)
    previous_guesses.append("_ _ _ _ _")

def filter_guesses(guess, diff, guesses):
    remaining_guesses = []
    unallowed_characters = []
    mandatory_characters = {}
    solved_characters = {}
    i = 0
    while(i < 5):
        if diff[i] == 2:
            solved_characters[guess[i]] = i
        elif diff[i] == 1:
            mandatory_characters[guess[i]] = i
        else:
            unallowed_characters.append(guess[i])
        i+=1

    for allowed_guess in guesses:
        invalid0 = False
        invalid1 = False
        invalid2 = False
        i = 0
        j = 0
        while i < len(unallowed_characters) and not invalid0:
            if unallowed_characters[i] in allowed_guess:
                #print(f"{allowed_guess} had {unallowed_characters[i]}, filtering out")
                invalid0 = True
            i += 1
        
        for character in mandatory_characters:
            if not character in allowed_guess:
                invalid1 = True
                break
            if allowed_guess[mandatory_characters[character]] == character:
                invalid1 = True
                break

        for character in solved_characters:
            if allowed_guess[solved_characters[character]] != character:
                invalid2 = True
                break
        if not (invalid0 or invalid1 or invalid2):
            remaining_guesses.append(allowed_guess)
            
    return remaining_guesses


def get_info(guess, patterns, allowed_guesses):
    information_for_guess = [0] * len(patterns)
    current_pattern = 0
    for pattern in patterns:
        #print(f"Testing pattern {pattern}")
        num_left = len(filter_guesses(guess, pattern, allowed_guesses))
        information_for_guess[current_pattern] = num_left
        current_pattern += 1
    #print(f"Info of first 5 out of {len(information_for_guess)} patterns: {information_for_guess[:5]}")
    return sum(information_for_guess)/len(information_for_guess)

def pad_to_5(num):
    if len(num) >= 5:
        return num
    num_to_pad = 5 - len(num)
    pad = ""
    for i in range(num_to_pad):
        pad += "0"
    return pad + num

def convert_to_base_3(num):
    converted_num = ""
    if num < 3:
        return pad_to_5(str(num))
    while num != 0:
        converted_num = str(num % 3) + converted_num
        num = int(num / 3)

    return pad_to_5(converted_num)

def string_pattern_to_array(num):
    pattern_array = []
    for char in num:
        pattern_array.append(int(char))
    return pattern_array

def enumerate_patterns():
    patterns = []
    current_pattern = 0
    while current_pattern < 243:
        string_pattern = convert_to_base_3(current_pattern)
        patterns.append(string_pattern_to_array(string_pattern))
        current_pattern += 1
    return patterns