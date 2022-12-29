'''
Lab 6 Version 1
Name: Tanishq
Description: The players take turns rolling five dice, and the player with the highest score wins'''

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

def main():
    """
    Main function.
    creates a random roll and then displays all of the information.
    """
    roll = make_roll()
    print(f"Rolling the dice... {roll}\nUpper section:")
    display_upper_section(fill_upper_section(roll))


if __name__ == "__main__":  #ensures that main is not run if file is imported
    main()