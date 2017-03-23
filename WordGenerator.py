import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
LETTERS = VOWELS+CONSONANTS

def assemble_word(user_options):
    generated_word = ""

    for option in user_options:
        if option == 'v':
            generated_word = generated_word + random.choice(VOWELS)
        elif option == 'c':
            generated_word = generated_word + random.choice(CONSONANTS)
        elif option == 'l':
            generated_word = generated_word + random.choice(LETTERS)
        else:
            generated_word = generated_word + option

    return generated_word;
