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
            if x > 0:
                print(f"Hint: {klingonTranslation[i][0] + '*'*(len(klingonTranslation[i])-2) + klingonTranslation[0][-1]}")
            yourTry = input()
            if yourTry == klingonTranslation[i]:
                print("Correct!")
                x = 3
            else:
                print(f"Sorry, you're wrong!")
                x += 1
'''
Same as the second one, but uses a counter and a while loop to see which attempt it's on. If its past the first attempt, it prints a hint.
I used the first and last letters of the correct answer, and multiplid * by the length of the word - 2.
'''