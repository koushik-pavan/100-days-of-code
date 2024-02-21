import pandas as pd

#TODO 1. Create a dictionary in this format:
nato_alpha = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {index.letter:index.code for (row, index) in nato_alpha.iterrows()}
#print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

loop_out = True
while loop_out:
    input_word = input("enter your word:")
    try:
        result = [nato_dict[x] for x in input_word.upper()]
    except KeyError:
        print("you might have entered symbols other than alphabet")
    else:
        print(result)
        break