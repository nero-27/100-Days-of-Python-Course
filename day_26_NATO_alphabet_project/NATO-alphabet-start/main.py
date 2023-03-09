import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:

# Loop through rows of a data frame

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


alpha = True
while alpha:
    try:
        word = input("Enter a word: ")
        result = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry. Please enter alphabets only.")
    else:
        print(result)
        alpha = False




