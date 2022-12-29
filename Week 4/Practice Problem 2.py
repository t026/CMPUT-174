import random
num_of_jelly_beans = random.randint(2000,5000)
sumnum = 0
for i in str(num_of_jelly_beans):
    sumnum += int(i)
x = 0
print(num_of_jelly_beans)
while x < 3:
    if x == 1:
        print(f"\nHint #1 \nSum of all digits: {sumnum}\n")
    if x == 2:
        print(f"\nHint #2 \nFirst digit: {str(num_of_jelly_beans)[0]}, Last digit: {str(num_of_jelly_beans)[-1]}\n")
    guess = int(input("How many jelly?:"))
    if guess == num_of_jelly_beans:
        if x == 0:
            coupon = 0.5
        elif x == 1:
            coupon = 0.2
        else:
            coupon = 0.1
        print(f"\nYou got a coupon of {int(coupon * 100)}%. Good Stuff Lad.")
        break
    elif x == 2:
        print("\nTough Luck")
    else:
        print("\nWrong")
    x += 1