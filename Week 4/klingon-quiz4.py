import random
with open ("klingon-english.txt", "r") as f:
    lineList = f.readlines()
klingonTranslation = []
englishTranslation = []
for i in lineList:
    line = i.split('|')
    klingonTranslation.append(str(line[0]).strip())
    englishTranslation.append(str(line[1]).strip())
while True:
    practiceConsonant = input("Which consonant do you want to practice with?\n")
    if practiceConsonant in ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 's', 't' 'v', 'w', 'y', "'"]:
        break
    else:
        print('Please enter a valid Klingon consonant.')
x = 0
while x < 3:        
    for i in range(len(klingonTranslation)):
        if str(klingonTranslation[i])[:len(practiceConsonant)] == practiceConsonant:
            print(f'How do you translate {englishTranslation[i]} to Klingon? You have {3-x} attempts left.')
            if x == 1:
                print(f"Hint: {klingonTranslation[i][0] + '*'*(len(klingonTranslation[i])-2) + klingonTranslation[0][-1]}")
            elif x == 2:
                hint = klingonTranslation[i][0] + '*'*(len(klingonTranslation[i])-2) + klingonTranslation[0][-1]
                j = random.randint(1, len(klingonTranslation[i])-1)
                hint = list(hint)
                hint[j] = klingonTranslation[i][j]
                print(f'Hint: {"".join(hint)}')
            yourTry = input()
            if yourTry == klingonTranslation[i]:
                print("Correct!")
                x = 3
            else:
                print(f"Sorry, you're wrong!")
                x += 1
                if x == 3:
                    print(f'The correct answer is {klingonTranslation[i]}')
'''
I created a list of the word and changed a random index in between to the correct letter for the second hint
I used the ranodom module to use randint function to find aa random number between 1 and the length of the word -1, so that it gives me a random index in between
'''