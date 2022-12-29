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
#stored these variables in two list
olderlist = []
#created another list for everyone who is older 
name = input("Enter your name:")
age = float(input("Enter your age:"))
#takes name and age as input
if age >= 0:
    for i in range(0, len(ages)):
        if age < ages[i]:
            olderlist.append(names[i])
    for i in olderlist:
        if i in names:
            names.remove(i)
#Iterates through the list to find out anyone who is older and appends them to the list, while removing them from the first list.
    if len(olderlist) != 0:
        if len(names) == 0:
            print(f"{name} is {round(age)} years old and they are younger than {', ' .join(olderlist)}")
            #prints suitable messages based on age
        else:
            print(f"{name} is {round(age)} years old and they are older than {', '.join(names)}")
            print(f"{name} is {round(age)} years old and they are younger than {', '.join(olderlist)}")
    else:
        print(f"{name} is {round(age)} years old and they are older than {', '.join(names)}")
else:
    print("Invalid age.")
#validates for -1