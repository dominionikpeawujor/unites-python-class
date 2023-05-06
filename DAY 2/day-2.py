# ========== DATA TYPES ==========
# Numeric Types: int, float, complex
# Text Type: str
# Sequence Types: list, tuple, range
# Mapping Type:	dict
# Set Types: set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type: NoneType

# ========== Numeric Data Types ==========
# Integer
# Float
# Complex

# ------ Integer ------ 
# Positive or negative whole numbers
# E.g.: 10, 120, -100, 50

int_number1 = 10
int_number2 = 20

int_answer = int_number1 + int_number2
print("Integer numbers: "+ str(int_answer))

# ------ Float ------ 
# Decimal numbers
# E.g: 10.3, 10.0, -100.9. etc
float_number1 = 100.9
float_number2 = 200.1

float_answer = float_number1 + float_number2
print( "Float numbers: "+ str(float_answer))

# ------ Complex ------ 
# Numbers with imaginary part
# E.g: 2+3j, 5+3i, etc

complex_number1 = 2+3j
complex_number2 = 3+4j
print(type(complex_number1))

complex_answer = complex_number1 + complex_number2
print("Complex numbers: " + str(complex_answer))


# ========== String Data Types ==========
# Text Type
# E.g.: "Hello", 'Hello'

fullname = "Daniel Benjamin"

# ------ String Operations ------ 
#Slicing
firstname = fullname[0:6]
lastname = fullname[7:]
print("Welcome, " + firstname)
print("Mr. " + lastname)

# Concatenation

# ===== SEQUENCE DATA TYPES =====
#list

person1 = 'shola'
person2 = 'ade'
person3 = 'sylvester'

person = ['shola', 'ade', 'sylvester']
person[0]