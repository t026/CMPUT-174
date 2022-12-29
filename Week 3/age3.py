pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901
name = input("Enter your name:")
age = float(input("Enter your age:"))
#i created two lists and messages for everyone younger and older than us.
older = []
younger = []
message1 = ''
message2 = ''
#compares age to each of the people and creates a message based on each condition.
if age != -1:
    if age > pippin_age:
        if age > frodo_age:
            if age > gollum_age:
                if age > arwen_age:
                    message1 = 'they are older than Arwen, Gollum, Frodo, Pippin.'
                else:
                    message1 = 'they are older than Gollum, Frodo, Pippin.'
                    message2 = 'they are younger than Arwen.'
            else:
                message1 = 'they are older than Frodo, Pippin.'
                message2 = 'they are younger than Arwen, Gollum.'
        else:
            message1 = 'they are older than Pippin.'
            message2 = 'they are younger than Arwen, Gollum, Frodo.'
    else:
        message2 = 'they are younger than Arwen, Gollum, Frodo, Pippin.'
    age = round(age)
    #checks length of each list and prints the suitable message.
    if len(older) != 0:
        if len(younger) == 0:
            print(f"{name} is {age} years old, and {message1}")
        else:
            print(f"{name} is {age} years old, and {message1}")
            print(f"{name} is {age} years old, and {message2}")
    else:
        print(f"{name} is {age} years old, and {message2}")
else:
    print("Invalid age")