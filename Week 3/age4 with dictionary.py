lotrDictionary = {'Legolas':2931, 'Gandalf':2000, 'Gimli':139, 'Aragorn':86, 'Frodo':50, 'Boromir':40, 'Samwise':38, 'Merry':36, 'Pippin':28}
#i used a dictionary to store the various names and ages. The name is the key and the age is the value.
name = input("Enter your name:")
age = float(input("Enter your age:"))
olderList = []
youngerList = []
#i added the prefix text to the list in the assignment statemnt to simplify things.
message1 = name + ' is ' + str(round(age)) + ' years old, and they are older than '
message2 = name + ' is ' + str(round(age)) + ' years old, and they are younger than '
#this is the same as age3, where I have two lists, one for anyone older and one for anyone younger. 
if age >= 0:
    for i in range(0, len(list(lotrDictionary.values()))):
        if age > list(lotrDictionary.values())[i]:
            olderList.append(list(lotrDictionary.keys())[i])
        else:
            youngerList.append(list(lotrDictionary.keys())[i])
#the code below adds the name of everyone older or younger to the respective list
    for j in range(0, len(olderList)):
        message1 += olderList[j]
        if j < len(olderList) - 1:
            message1 += ', '
        elif j == len(olderList) - 1:
            message1 += '.'
    for k in range(0, len(youngerList)):
        message2 += youngerList[k]
        if k < len(youngerList) - 1:
            message2 += ', '
        elif k == len(youngerList) - 1:
            message2 += '.'
    #this if statement decides which messages to print based on how many people are older/younger than us.
    if len(olderList) != 0:
        if len(youngerList) == 0:
            print(message1)
        else:
            print(message1)
            print(message2)
    else:
        print(message2)
else:
    print("Invalid age.")