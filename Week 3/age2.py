frodo_age = 51
gollum_age = 589
name = input("Enter your name:")
age = float(input("Enter your age:"))
#the if statement compares it to both Frodo and Gollum
if age > frodo_age and age > gollum_age:
    message = "they are older than Frodo and Gollum."
elif age > frodo_age and age < gollum_age:
    message = "they are older than Frodo but they are younger than Gollum."
else:
    message = "they are younger than Frodo and Gollum."
print(f"{name} is {round(age)} years old, and they are {message}")
