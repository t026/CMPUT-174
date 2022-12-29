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

attempt = 1
while attempt < 4: 
    print(attempt)
    for i in range(len(Klingon)):
        klingon_word_consonant = Klingon[i][:len(users_consonant)]
        if users_consonant == klingon_word_consonant:
            if attempt == 2:
                hint = Klingon[i][0]
                hint +=  (len(Klingon[i])-2) *'*'
                hint += Klingon[i][-1]
                print(f"Hint: {hint}")
            if attempt == 3:
                import random
                n = random.randint(1, len(Klingon[i]) - 1)
                hint = Klingon[i][0]
                hint +=  (len(Klingon[i])-2) *'*'
                hint += Klingon[i][-1]
                hint = list(hint)
                hint[n] = Klingon[i][n]
                hint = str(hint)
                print(f"Hint:{hint}")
            print(f"How do you translate {English[i]} to Klingon? You have {4 - attempt} attempts left.")
            v = input()
            if v == Klingon[i]:
                print("Correct!")
                attempt = 5
            else:
                print("Sorry, you're wrong!")
                attempt += 1
            if attempt == 4:
                print(f"The correct answer is {Klingon[i]}")
