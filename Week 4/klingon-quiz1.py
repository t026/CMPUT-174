with open("klingon-english.txt", "r") as f:
    lineList = f.readlines()
    correctAnswer = lineList[2].split('|')[0].strip()
#i used with so that it closes the file immediately.
usersTranslation = input("How do you translate computer to Klingon?\n")
#\n creates a new line for more readable output and input
if usersTranslation.strip() == correctAnswer:
    print("Correct!")
else:
    print(f"Sorry, the correct answer is {correctAnswer}.")
#checks if correct or not, and prints correct answer.