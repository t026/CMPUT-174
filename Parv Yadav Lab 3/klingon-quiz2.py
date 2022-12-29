'''
Opens the file to read and creates a list of all lines in  file. That way I can close file.
'''
file = open ("klingon-english.txt", "r")
list_of_lines = file.readlines()
file.close()
'''
First two lists are parallel lists with klingon and english translations of same word. 
Third list is for klingon consonants to valiate user input
.strip() removes the \n from the line
'''
Klingon = []
English = []
Klingon_Consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 's', 't' 'v', 'w', 'y', "'"]

for i in list_of_lines:
    i = i.strip()
    i = i.split('|')
    Klingon.append(i[0])
    English.append(i[1])
'''
uses while loop to validate user inputs correct consonant.
'''
x = 0
while x == 0:
    users_consonant = input("Which consonant do you want to practice with?")
    if users_consonant not in Klingon_Consonants:
        print('Please enter a valid Klingon consonant.')
    else:
        x = 1

'''
looks through klingon list to find a word with correct consonant and validates user input
'''
for i in range(len(Klingon)):
    klingon_word_consonant = Klingon[i][:len(users_consonant)]
    if users_consonant == klingon_word_consonant:
        print(f"How do you translate {English[i]} to Klingon?")
        v = input()
        if v == Klingon[i]:
            print("Correct!")
        else:
            print("Sorry, you're wrong!")
            print(f"The correct answer is {Klingon[i]}")
        