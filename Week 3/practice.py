#temperature = float(input("Enter the temperautre in degrees celsius:"))
#if temperature < -5:
#   print("Wear your jacket")
#print("Enter classroom.")
#name = input("Enter your first name.")
#if name[0] > 'm':
#    print(f'{name} will sit in the right side.')
#else:
#    print(f'{name} will sit in the left side.')
classAverage = float(input("Enter the class average:"))
if classAverage <= 40:
    sweet = 'lollipops'
elif classAverage <= 90:
    sweet = 'cookies'
else:
    sweet = 'ice cream'
print(f'Mr Ratburn will need to bring {sweet}.')