import random
def display_header(string:str)-> None:
    '''Prints the header'''
    print(f"+{'-'*len(string)}+")
    print(f"|{string}|")
    print(f"+{'-'*len(string)}+")
def ask_a_question() -> bool:
    '''prompts the student with the question.
    Returns True if answer is correct and False otherwise'''
    operators = ('*', '+', '-')
    op = random.choice(operators)
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    question = f"{x} {op} {y}:"
    answer = int(input(question))
    if op == '+':
        correct_answer = x + y
    elif op == "-":
        correct_answer = x - y
    else:
        correct_answer = x * y
    return answer == correct_answer # THROWS True or False
def main():
    display_header("Math is Fun-Ends")
    print(ask_a_question()) # CATCH
main()