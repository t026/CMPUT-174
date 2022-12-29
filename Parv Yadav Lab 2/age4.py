names = [
    "Frodo",
    "Samwise",
    "Gandalf",
    "Legolas",
    "Gimli",
    "Aragorn",
    "Boromir",
    "Merry",
    "Pippin",
]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
#2 list with matching indexes
character_name = input("Enter the character's name: ")
character_age = int(input("Enter the character's age: "))
everyone_older = []
everyone_younger = []
if character_age >= 0:
    for i in range(0, len(ages)):
        if character_age > ages[i]:
            everyone_younger.append(names[i])
        else:
            everyone_older.append(names[i])
    younger_people = ', '.join(everyone_younger)
    older_people = ', '.join(everyone_older)
    if len(everyone_older) > 0 and len(everyone_younger) > 0:
        print(f"{character_name} is {round(character_age)} years old and they are older than {younger_people}")
        print(f"{character_name} is {round(character_age)} years old and they are younger than {older_people}")
    elif len(everyone_older) > 0 and len(everyone_younger) == 0:
        print(f"{character_name} is {round(character_age)} years old and they are younger than {older_people}")
    else:
        print(f"{character_name} is {round(character_age)} years old and they are older than {younger_people}")
else:
    print("Invalid age")
'''iterates through the age list and adds the name to the respective lists based on if its younger or older
then prints suitable message based on length of list'''