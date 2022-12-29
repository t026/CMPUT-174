frodo_age = 51
name = input("Enter your name:")
age = float(input("Enter your age:"))
#uses if statements to compare our age to frodo and prints the respective message using an f-string
if age > frodo_age:
    message = 'they are older than Frodo Baggins.'
elif age < frodo_age:
    message = 'they are younger than Frodo Baggins.'
else:
    message = 'they are of the same as Frodo Baggins.'
print(f"{name} {round(age)} years old, and {message}")
