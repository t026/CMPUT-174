import random
NUMBER_OF_QUESTIONS = 3
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
def ask_questions() -> int:
    '''Asks three questions and returns the quiz score'''
    quiz_score = 0 
    for index in range(NUMBER_OF_QUESTIONS):
        result = ask_a_question() # CATCH
        if result:
            print("Correct")
            quiz_score = quiz_score + 1
        else:
            print("Incorrect")
    print(f"Quiz Score : {quiz_score}/{NUMBER_OF_QUESTIONS}")
    return quiz_score
def run_quiz(scores: list, count: int)-> None:
    '''
    This function is an example of when a function has a side effect
    We are changing an existing mutable object.
    We do not need to return this mutable object.
    The side effect of the append will be known to the main function.'''
    print(f'Quiz {count}')
    input("Press any key to start the attempt.")
    quiz_score = ask_questions()
    scores.append(quiz_score)
def main():
    scores = []
    count = 1
    display_header("Math is Fun-Starts")
    run_quiz(scores, count)
    print(scores)
    continue_testing = True
    while continue_testing:
        reply = input("Continue y/N > :").lower()
        continue_testing = reply == 'y'
        if continue_testing:
            count += 1
            display_header("Math is Fun-Continues")
            run_quiz(scores, count)
    display_header("Math is Fun-Ends")
main()
'''Practice Question, Display highest scores and which quizes they were obtained in.'''