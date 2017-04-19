import wordgenerator

NUMBER_OF_WORDS = int(input("How many random words do you want? "))
NUMBER_OF_LETTERS = int(input("How many letters do you want the random words to have? "))

user_options = list()
for i in range(0 , NUMBER_OF_LETTERS):
    user_choice = input("What letter " + str(i + 1) + " do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
    user_options.append(user_choice)

for i in range(0, NUMBER_OF_WORDS):
    word = wordgenerator.assemble_word(user_options)
    print(word)
