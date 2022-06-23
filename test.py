sentence = input('Enter the text: ')
all_words = sentence.split()
length_longest_word = 0

for word in all_words:
    count = 0
    small_letter_word = ''
    for letter in word:
        if letter.islower():
            count += 1
            small_letter_word += letter
        else:
            if count >= length_longest_word:
                length_longest_word = count
                lon_small_letter_word = small_letter_word
            count = 0
            small_letter_word = ''
    if count >= length_longest_word:
        length_longest_word = count
        lon_small_letter_word = small_letter_word

# print(length_longest_word)
print(f"The longest continuous series of small alphabetic letters is: {lon_small_letter_word}")