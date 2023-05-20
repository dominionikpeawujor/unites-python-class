# =========== PROJECT ===========
# Building a simple integer calculator with python

# ======= PROJECT OUTCOME =======

# CTRL + / -  FORWARD SLASH

## At the End
# - Receiving user input ✅
# - Type casting - converting a value in one data type to another ✅
# - If-else statements ✅
# - Boolean expressions ✅
# - Switch cases (Match-Case in Python)✅
# - Reassignments ✅
# - Algorithm ✅
# - Loops - While ✅
# - List - SIGNS ✅
# - Concatenation ✅
# - GitHub ⏳

### ======== LOOPS ======== 
## For loop - uses a range of values

# numbers = [1,2,3,4]
# range(1,100) = [1,2,...,99]
# E.G.: for number in numbers:
#     print(number)

## While loop - uses boolean expressions
# number = 1000
# while(number % 2 == 0):
#     number = number / 2
#     print(number)
#        print('hello world')

### ======== SWITCH ========
# value = input('enter a value: ')
# match value:
#     case 'value_1':
#         print('value_1')
#     case 'value_2':
#         print('value_2')
#     case _:
#         print('invalid')


# ========= SOLUTION =========

# ========= Algorithm =========

# --- Legend ---
# ✅ - Completed 
# ⏳ - Pending

# ---------------------------

# - STEP 1: Take user input ✅
# --- First Number ✅
# --- Arithmetic sign ✅
# ------ Define a 'SIGNS' list = ['+','-','/','*'] ✅
# ------ if user arithmetic sign input is not in SIGNS list, print invalid, try again✅
# --- Second Number✅

# - STEP 2: Carry out operation based on user arithmetic sign input✅
# ---- Match-Case✅
# --- if arithmetic sign input is '+', answer = first number + second✅
# --- if arithmetic sign input is '-', answer = first number - second✅
# --- if arithmetic sign input is '*', answer = first number * second✅
# --- if arithmetic sign input is '/', answer = first number / second✅
# --- if arithmetic sign input is invalid, print Invalid input. Try again✅

# - STEP 3: Print out answer✅



# =========================== CODE SOLUTION ===========================

# -------------- STEP 1: Take user input ✅ -------------------------

SIGNS = ['*', '+', '-', '/'] # - List of legal arithmetic signs
answer = 0 # - answer variable
response = 'y' # - Ask user to restart calculator 

while (response == 'y'):
    ## ===== Take user input =====
    # Receiving user input & Type casting into an integer

    firstNumber = int(input("Enter the first number: ")) # Receiving first number

    # - Checking if arithmetic sign is in SIGNS list
    isThereanyIncorrectSign = True # Boolean Expression

    while (isThereanyIncorrectSign == True): # While Loop 
        arithmeticSign = input("Enter Arithmetic Sign: ")  # - Receiving arithmetic input
        if arithmeticSign not in SIGNS: # if-else statement
            print('Invalid input. Try again')
        else:
            isThereanyIncorrectSign = False # Variable Reassignment

    secondNumber = int(input("Enter the second number: ")) # Receiving second number


    # ------- STEP 2: Carry out operation based on user arithmetic sign input  ✅ -------
    # ---- Match-Case ✅ -------
    match arithmeticSign: 
        case '+':
            answer = firstNumber + secondNumber
        case '-':
            answer = firstNumber - secondNumber
        case '/':
            answer = firstNumber / secondNumber
        case '*':
            answer = firstNumber * secondNumber
        case _:  # the default value
            print('Invalid input. Try again') # This is just an example of the default case. It is redudant in this code

    # -------------- STEP 3: Print out answer ✅ --------------
    # Type casting from integer to string & Concatenation
    print("The Answer to",str(firstNumber), arithmeticSign , str(secondNumber) , "equals to", str(answer)) # Concatenation

    # - Ask user to restart calculator
    response = input("Do you want to calculate another value? (y/n) ") # Variable Reassignment



# ---- SIDE NOTES ----
# Validating user input in python

# codewars.com
# hackerrank.com