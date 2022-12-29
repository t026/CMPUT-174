pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901

character_name = input("Enter the character's name:")
character_age= float(input("Enter the character's age:"))
#float() function converts the value from string to float to allow for operations with decimal numbers

if character_age >= 0:
    if character_age > pippin_age and character_age > frodo_age and character_age > gollum_age and character_age > arwen_age:
        print(f"{character_name} is {round(character_age)} years old, and they are older than Arwen, Gollum, Frodo, Pippin")
    elif character_age > pippin_age and character_age > frodo_age and character_age > gollum_age and character_age < arwen_age:
        print(f"{character_name} is {round(character_age)} years old, and they are older than Gollum, Frodo, Pippin")
        print(f"{character_name} is {round(character_age)} years old, and they are younger than Arwen")
    elif character_age > pippin_age and character_age > frodo_age and character_age < gollum_age and character_age < arwen_age:
        print(f"{character_name} is {round(character_age)} years old, and they are older than Frodo, Pippin")
        print(f"{character_name} is {round(character_age)} years old, and they are younger than Arwen, Gollum")
    elif character_age > pippin_age and character_age < frodo_age and character_age < gollum_age and character_age < arwen_age:
        print(f"{character_name} is {round(character_age)} years old, and they are older than Pippin")
        print(f"{character_name} is {round(character_age)} years old, and they are younger than Arwen, Gollum, Frodo")
    else:
        print(f"{character_name} is {round(character_age)} years old, and they are younger than Arwen, Gollum, Frodo, Pippin")
#round() function because the demo printed whole numbers.
else:
    print('Invalid Age')
#outputs if negative