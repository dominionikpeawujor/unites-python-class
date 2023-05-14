# ========= BOOLEAN EXPRESSIONS =========
# Boolean simply means true or false 
# True
# False

number1 = 10
number2 = 10

# ========= OPERATORS =========
# Arithemtic Operators - +, - , /, *
# Comparison Operators - ==, >, <, !=, >=, <=
# Assignment Operators - =
# Logical Operators - in, etc
# Bitwise Operators - <<, >>
# Identity Operators - is, is not

# === COMPARISON OPERATIONS ===
print(number1 != number2) #False
print(number1 == number2) #True
print(number1 > number2) #False
print(number1 >= number2) #True
print(number1 <= number2) #True


# https://www.w3schools.com/python - Operators

# ========= CONDITIONALS =========
# if statements
# if - else statements
# if - elif - else statements


# ========= IF SYNTAX =========
if(number1 == number2):
    print("Numbers are equal")

# ====== IF-ELSE SYNTAX ====== 
name1 = 'habeeb'
print(name1 == 'daniel')

if(name1 == 'daniel'):
    print('Welcome Daniel')
else:
    print("It is not daniel.")

# ====== IF-ELIF-ELSE SYNTAX ======

name2 = input('Enter name: ')
if(name2 == 'daniel'):
    print('Welcome Daniel')
elif(name2 == 'habeeb'):
    print('Welcome Habeeb')
elif(name2 == 'sylvester'):
    print('Welcome Sylvester')
elif(name2 == 'jola'):
    print('Welcome Jola')
else:
    print("I don't know you ooo!")

# ===== TASK ===== 
# Write a program that prints out the health of a patient based on temperature
# if temperature is below 35 degrees celsius, print "under fever"
# if temperature is between 35 and 40, print "moderate fever"
# if temperature is between 40 and 45, print "high fever"
# else, print incorrect input


# Expo
temperature = int(input("Enter Temperature: "))
