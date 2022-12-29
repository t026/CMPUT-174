frodo_age = 51

character_name = input("Enter the character's name:")
character_age= float(input("Enter the character's age:"))
#float() function converts the value from string to float to allow for operations with decimal numbers

if character_age == frodo_age:
    print(f"{character_name} is {round(character_age)} years old, and they are of the same age as Frodo.")
elif character_age > frodo_age:
    print(f"{character_name} is {round(character_age)} years old, and they are older than Frodo.")
else:
    print(f"{character_name} is {round(character_age)} years old, and they are younger than Frodo.")
#round() function because the demo printed whole numbers.