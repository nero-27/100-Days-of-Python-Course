#TODO: Create a letter using starting_letter.txt
names = []

with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as invited_names:
    for line in invited_names:

        name = line.strip('\n')
        names.append(name)

for name in names:
    with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as starting_letter:
        text = starting_letter.read()
        text = text.replace('[name]', name)
        with open(f'../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt', 'w') as send_letter:
            send_letter.write(text)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp