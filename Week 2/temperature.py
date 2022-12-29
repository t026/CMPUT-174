tempC = float(input("Enter the temperature in degrees celsius:"))
#uses float incase decimal is included
tempF = round((tempC*9/5)+32)
#uses round to get whole number
print(f"{round(tempC)} degrees in Canada would be {tempF} degrees in Springfield. D'oh!")
#uses fstring to include variable values in output.