'''
Opens the file to read and creates a list of all lines in the file. That way I can close the file after since I don't need it.
'''
file = open ("klingon-english.txt", "r")
list_of_lines = file.readlines()
file.close()

'''
Asks for user input and prints whether its correct or not based on input
'''
computer_in_klingon = list_of_lines[2].split('|')[0]
user_input = input("How do you translate computer to Klingon?")
if user_input == computer_in_klingon:
    print('Correct!')
else:
    print("Sorry, you're wrong!")
    print(f"The correct answer is {computer_in_klingon}.")