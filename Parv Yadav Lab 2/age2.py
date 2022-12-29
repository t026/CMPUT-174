frodo_age = 51
gollum_age = 589

character_name = input("Enter the character's name:")
character_age= float(input("Enter the character's age:"))
#float() function converts the value from string to float to allow for operations with decimal numbers

if character_age > frodo_age and character_age > gollum_age:
    print(f"{character_name} is {round(character_age)} years old, and they are older than Frodo and Gollum.")
elif character_age > frodo_age and character_age < gollum_age:
    print(f"{character_name} is {round(character_age)} years old, and they are older than Frodo but younger than Gollum.")
else:
    print(f"{character_name} is {round(character_age)} years old, and they are younger than Frodo and Gollum.")
#round() function because the demo printed whole numbers.