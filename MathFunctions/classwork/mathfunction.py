# Math Functions in Python
# 💡 What are Math Functions?

# Math functions are built-in tools Python gives us to perform calculations without writing everything ourselves.
# They make working with numbers easier and faster — like having a calculator inside Python!

# There are two main types:

# Built-in math functions — already available without importing anything.

# Functions from the math module — we must import the math library to use them.

# Built-in Math Functions

# These come ready to use:

# Function	Description	                                            Example	Output
# abs(x)	Returns the absolute (positive) value of x	            abs(-5) 	5
print("Math Functions in Python abs =>", abs(-10))
# round(x)	Rounds a number to the nearest whole number	            round(4.6)	5
print("Math Functions in Python round =>", round(4.3))
# max(a, b, c, …)	Returns the largest number	                    max(4, 10, 6)	10
print("Math Functions in Python max =>", max(4, 10, 6))
# min(a, b, c, …)	Returns the smallest number	                    min(4, 10, 6)	4
print("Math Functions in Python min =>", min(4, 10, 6))
# pow(a, b)	Returns a raised to the power of b	                    pow(2, 3)	8
# inputOne = int(input("Enter base number for power function: "))
# inputTwo = int(input("Enter exponent number for power function: "))
# print("Math Functions in Python pow =>", pow(inputOne, inputTwo))
print("Math Functions in Python pow =>", pow(2, 4))

# Math Module Functions

# For more advanced operations, we need to import the math module:

# import math

# Function	    Description	                             Example	        Output
# math.sqrt(x)	Square root of x	                     math.sqrt(25)	    5.0
# math.floor(x)	Rounds down to the nearest whole number	math.floor(4.9)	    4
# math.ceil(x)	Rounds up to the nearest whole number	math.ceil(4.1)	    5
# math.pi	    Returns the constant π (pi = 3.14159...)	math.pi	            3.14159...
# 💻 Example:
import math

number = -9

print(abs(number))       # 9
print(round(4.7))        # 5
print(max(2, 8, 5))      # 8
largeNumber  = int(input("Enter a large number to get its square root: "))
roundedValue = math.sqrt(largeNumber)
print("The square root of the large number is  =>",math.sqrt(largeNumber))
print("The rounded number for the square root is  =>",round(roundedValue))
print(math.sqrt(16))     # 4.0
print(math.floor(4.8))   # 4
print(math.ceil(4.1))    # 5
