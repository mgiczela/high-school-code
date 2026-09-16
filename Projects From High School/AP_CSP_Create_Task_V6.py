import random
import sys


def print_instructions():
    """ Prints instructions for how to play.

    Returns:
        N/A: Nothing is returned.
    """
    print('''
    Welcome to the Basic Math Operation Practice Game!
    In this game, you can practice your basic math skills in addition, subtraction, division and multiplication.
    --------------------------------------------------------------------------------------------------------------
    You will be able to customize your practice session to suit your needs!
    You can choose the range, operation and number of problems to give a more personalized practice experience.
    ---------------------------------------------------------------------------------------------------------------
    After answering all the problems, you will be able to retry any problems you got wrong!
    The program scores you on how many questions and retry questions you answer correctly.
    There is also bonus points if you get all the questions correctly the first try!
    --------------------------------------------------------------------------------------------------------------
    ''')
    ready_to_play = input("When you have read all the instructions, press the enter key when you are ready to start practicing. ")
    while ready_to_play != "":
        ready_to_play = input("When you have read all the instructions, press the enter key when you are ready to start practicing. ")
    print("")

def get_num_questions():
    """ Gets how many questions to answer from User, ensures input is valid.

    Returns:
        num_problems(int): how many problems the user wants to answer.
    """
    num_problems = -1.5
    while type(num_problems) is not int:
        num_problems = input("How many problems would you like to answer? Please enter an integer! ")
        try:
            num_problems = int(num_problems)
        except ValueError:
            num_problems = num_problems
    return num_problems

def get_operation():
    """ Gets mathematical operation from User, ensures input is valid.

    Returns:
        operation(string): The mathematical operation the User wishes to practice.
    """
    operation = input("Would you like to practice? (Respond with \"+\" or \"-\" or \"/\" or \"x\") ") 
    while operation != "+" or operation != "-" or operation != "/" or operation != "x":
        if operation == "+" or operation == "-" or operation == "/" or operation == "x":
            break 
        else:
            operation = input("Invalid Input! (Respond with \"+\" or \"-\" or \"/\" or \"x\") ")
    return operation

def get_range():
    """ Gets minimum and maximun numbers that problems are generated with from the user, ensures input is valid and that min < max

    Returns:
        min(int): The minimum (The lowest number generated in problems).
        max(int): The maximimum (The highest number generated in the problems)
    """
    min = -0.1
    while type(min) is not int:
        min = input("What is the lowest number you want in your problems? Please enter an integer! ")
        try:
            min = int(min)
        except ValueError:
            pass
    ##########################################################
    # Getting the max of numbers to generate problems from #
    ##########################################################
    max = -0.1
    while type(max) is not int:
        max = input("What is the highest number you want in your problems? Please enter an integer! ")
        try:
            max = int(max)
        except ValueError:
            pass
    while max < min:
        max_temp = input("What is the highest number you want in your problems? Please enter an integer that is >= to the minimum! ")
        try:
            max = int(max_temp)
        except ValueError:
            pass
    if oppr == "/": 
        while max == min and max == 0:
            max_temp2 = input("For division, you cannot enter a range of just 0, please try again! ")
            try:
                max = int(max_temp2)
            except ValueError:
                pass
    return min, max

def generate_question(oppr, min_range, max_range):
    """ Generate 2 random integers within user-selected range to form a mathematical problem with the user-selected operation.

    Args:
        oppr (string): The mathematical opperation (+,-,/,x) the pogram uses.
        min_range (int): The minimum number that the program will generate problems with.
        max_range (int): The maximum number that the program will generate problems with.

    Returns:
        num1(int): First number in the problems
        num2(int): Second number in the problems
        solution(int): The result of preforming the user-selected operation on num1 and num2.
    """
    num1 = random.randint(min_range, max_range)
    num2 = random.randint(min_range, max_range)
    if oppr == "+":
        solution = num1 + num2
    elif oppr == "-":
        num2 = random.randint(min_range, num1)
        solution = num1 - num2
    elif oppr == "x":
        solution = num1 * num2
    elif oppr == "/":
        while num2 == 0:
            num2 = random.randint(min_range, max_range)
        solution = int((num1 * num2) / num2)
    return num1, num2, solution

def get_user_response(oppr, solution, num1, num2, errors, pts_question, correct_answers):
    """ Prints questions for the user, gets responses & checks if user's responses are wrong, adds errors to a list and returns that list.

    Args:
        oppr (string): The mathematical opperation (+,-,/,x) the program uses.
        num1(int): First number in the problems.
        num2(int): Second number in the problems.
        pts_question(int): Points from each question.
        errors(list of int): List of the numbers used in problems the user got wrong.
        correct_answers(int): How many correct responses the user enters.

    Returns:
        pts_question(int): Points from each question.
        errors(list of int): List of the numbers used in problems the user got wrong.
        correct_answers(int): How many correct responses the user enters.
    """
    if oppr == "/":
        user_response = input(str(num1 * num2) + " / " + str(num2) + " = ")
    else: 
        user_response = input(str(num1) + " " + str(oppr) + " " + str(num2) + " = ")
    
    #tries to convert user input to integer
    try:
        user_response = int(user_response)
    except ValueError:
        user_response = user_response
    #if user gets question wrong, add that question to list of errors, if user gets it correct, give em 10 points and add 1 to num_correct
    if user_response != solution:
        errors.append((num1, num2))
    else:
        pts_question = pts_question + 10
        correct_answers += 1
    return errors, pts_question, correct_answers

def print_game_stats(correct_answers, errors, retries_correct, pts_question, num_of_questions):
    """ Prints statistics from the game, such as how many problems user got right first try and on retry, and their score.

    Args:
        retries_correct(int): How many retries the user got correct.
        num_of_questions(int): How many questions are generated in one run of the game.
        pts_question(int): Points from each question.
        errors(list of int): List of the numbers used in problems the user got wrong.
        correct_answers(int): How many correct responses the user enters.

    Returns:
        N/A: Nothing is returned
    """
    print("")
    print("Great Practice! Here are some facts from your practice session:")
    print("You answered " + str(correct_answers) + "/" + str(num_of_questions) + " correct first try, each worth 10 points.")
    if len(errors) >= 1:
        print("You answered " + str(retries_correct) + "/" + str(len(errors)) + " correct second try, each worth 5 points.")
    else:
        print("You made no errors! This is worth an extra point for each of the " + str(num_of_questions) + " questions you answered!")
    print("Your score was: " + str(pts_question))
    print("")

def create_and_check_retries(errors, pts_question, retries_correct, oppr):
    """ Prints problems user got wrong as retry, checks if they are correct.

    Args:
        retries_correct(int): How many retries the user got correct.
        oppr(string): The mathematical opperation (+,-,/,x) the program uses.
        pts_question(int): Points from each question.
        errors(list of int): List of the numbers used in problems the user got wrong.
        correct_answers(int): How many correct responses the user enters.

    Returns:
        pts_question(int): Points from each question.
        retries_correct(int): How many retries the user got correct.

    """
    for error in errors:
        if oppr != "/":
            user_retry = input(str(error[0]) + " " + str(oppr) + " " + str(error[1]) + " = ")
        elif oppr == "/":
            user_retry = input(str(error[0] * error[1]) + " / " + str(error[1]) + " = ")
        try:
            user_retry = int(user_retry)
        except ValueError:
            pass  
        #Get the solutions for the errors
        if oppr == "+":
            retry_sum = error[0] + error[1]
        elif oppr == "-":
            retry_sum = error[0] - error[1]
        elif oppr == "x":
            retry_sum = error[0] * error[1]
        elif oppr == "/":
            retry_sum = ((error[0] * error[1]) / error[1])
        #Tell user if they got retry right/wrong
        if user_retry == retry_sum:
            print("Great Job! You nailed that one!")
            pts_question += 5
            retries_correct += 1
        else:
            if oppr == "+" or oppr == "x" or oppr == "-":
                print("Oh No! " + str(error[0]) + " " + str(oppr) + " " + str(error[1]) + " = " + str(retry_sum))
            if oppr == "/":
                print("Oh No! " + str(error[0] * error[1]) + " / " + str(error[1]) + " = " + str(int(retry_sum)))
    return pts_question, retries_correct



""" NOTE: This comment goes with the play_game() function. :)
     The master function. Runs all other functions, this actually makes things happen.

    Args:
        num_of_questions(int): How many questions are generated in one run of the game.
        oppr(string): The mathematical opperation (+,-,/,x) the program uses.
        min_range(int): The minimum (The lowest number generated in problems).
        max_range(int): The maximimum (The highest number generated in the problems)

    Returns:
        pts_question(int): Points from each question.

"""
def play_game(num_of_questions, oppr, min_range, max_range):
    errors = []
    pts_question = 0
    correct_answers = 0
    retries_correct = 0
    if oppr == "+":
        print("You have selected: ADDITION (+)")
    elif oppr == "-":
        print("You have selected: SUBTRACTION (-)")
    elif oppr == "x":
        print("You have selected: MULTIPLICATION (x)")
    elif oppr == "/":
        print("You have selected: DIVISION (/)")
    for i in range(num_of_questions):
        num1, num2, solution = generate_question(oppr, min_range, max_range)
        errors, pts_question, correct_answers = get_user_response(oppr, solution, num1, num2, errors, pts_question, correct_answers)
    #retries code
    #RETRIES CODE
    if len(errors) >= 1:
        print("Here are all the questions you got wrong. Give them another try!")
        pts_question, retries_correct = create_and_check_retries(errors, pts_question, retries_correct, oppr)
    else:
        print("You did not make any errors! Excellent :)")
        pts_question = pts_question + (num_of_questions)

        
    print_game_stats(correct_answers, errors, retries_correct, pts_question, num_of_questions)
    return pts_question


print_instructions()
pts_total = 0 #set the total points to 0
play_status = "yes"

while play_status != "no": #this makes the while loop run until the user inputs "no" (meaning they dont want to practice more)
    num_of_questions = get_num_questions() #get the # of problems, make sure the input is valid.
    oppr = get_operation() #get the operation
    min_range, max_range = get_range() #get the range, make sure valid input
    pts_game = play_game(num_of_questions, oppr, min_range, max_range) #run function to play the game
    pts_total += pts_game
    play_status = input("Do you want to practice some more? (Respond with \"yes\" or \"no\") ")

#when the user inputs no (meaning they dont want to practice more):
print("Thanks for playing! I hope this practice helps you on your next test!")
print("The combined score from your practice session was: " + str(pts_total) + " points. Great Job!")