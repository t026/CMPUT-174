with open ("klingon-english.txt", "r") as f:
    lineList = f.readlines()
klingonTranslation = []
englishTranslation = []
#parallel lists for different translations
for i in lineList:
    line = i.split('|')
    klingonTranslation.append(str(line[0]).strip())
    englishTranslation.append(str(line[1]).strip())
#goes through file and adds to each list
while True:
    practiceConsonant = input("Which consonant do you want to practice with?\n")
    if practiceConsonant in ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 's', 't' 'v', 'w', 'y', "'"]:
        break
    else:
        print('Please enter a valid Klingon consonant.')
#looks for consonant in a list of all consonants.
for i in range(len(klingonTranslation)):
    if str(klingonTranslation[i])[:len(practiceConsonant)] == practiceConsonant:
        yourTry = input(f'How do you translate {englishTranslation[i]} to Klingon?')
        if yourTry == klingonTranslation[i]:
            print("Correct!")
        else:
            print(f"Sorry, you're wrong! \nThe correct answer is {klingonTranslation[i]}")
#looks for user input and prints respective message.