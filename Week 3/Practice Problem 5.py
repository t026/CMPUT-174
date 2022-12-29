quizmark = float(input("Enter the quiz mark:"))
if quizmark >= 50:
    participation = input("Enter the participation grade:")
    if participation.upper() == 'N':
        print("Quiz mark remains unchanged.")
    elif participation.upper() == 'A':
        newquizmark = quizmark*1.2
    elif participation.upper() == "U":
        newquizmark = quizmark*1.15
    elif participation.upper() == "S":
        newquizmark = quizmark*1.1
    elif participation.upper() == "R":
        newquizmark = quizmark* 1.05
    if newquizmark != quizmark:
        print(f"Your new quiz mark is {round(newquizmark)}")
else:
    print("Quiz mark remains unchanged.")
