'''
Lab 6 Version 3
Name: Tanishq
Description: Checks for three of a kind, four of a kind and yahtzee.
'''
import random

def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    return tuple(random.randint(1, 6) for index in range(0, 5))

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    The count(number) method returns how many times the number appears in the tuple. Multiply this by the number to get the sum.
    """
    return number*(roll.count(number))

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    A for loop in range(1, 7) to get a range of 1-6 and then call the sum_of_given_number each time with a different number.
    """
    mylist = []
    for i in range(1, 7):
        mylist.append(sum_of_given_number(roll, i))
    return mylist    

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    print(f"Aces: {upper_section_scores[0]}\nTwos: {upper_section_scores[1]}\nThrees: {upper_section_scores[2]}\nFours: {upper_section_scores[3]}\nFives: {upper_section_scores[4]}\nSixes:{upper_section_scores[5]}")

def num_of_a_kind(roll: tuple, number: int) -> int:
    '''
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all of their values. Otherwise, returns 0.
    First calls the fill_upper_section to obtain a list with all of the sums.
    Then checks if any sum divides by 3 to give the number. 
    If that is the case, returns the sum, otherwise returns 0
    '''
    upper_section = fill_upper_section(roll)
    for i in range(len(upper_section)):
        if upper_section[i]/(i+1) == number:  #i+1 because the counter starts at 0 and is therefore 1 step behind
            return sum(upper_section)
    return 0

def yahtzee(roll: tuple) -> int:
    '''
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    Looks through a for loop in the range(1, 7) and checks if the sum of the number is equal to the number * the length of the list
    '''
    for i in range(1, 7):
        if sum_of_given_number(roll, i) == i*len(roll):
            return 50
    return 0

def main():
    """
    Main function.
    """
    # Version 1 code
    roll = make_roll()  #creates a constant with random values.
    print(f"Rolling the dice... {roll}\nUpper section:")
    display_upper_section(fill_upper_section(roll))
    print(f"Lower Section:\nThree of a kind: {num_of_a_kind(roll, 3)}\nFour of a kind: {num_of_a_kind(roll, 4)}\nYahtzee: {yahtzee(roll)}")

if __name__ == "__main__":  #ensures that main is not run if the file is imported.
    main()