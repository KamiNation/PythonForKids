# What Is a String in Python?
# A string is like a sentence or word wrapped in quotes.


# Think of it as a gift box for words, letters, numbers, 
# emojis anything you want to say!
# As long as it’s inside quotation marks (" " or ' '), 
# Python treats it as a string.


# we use the "", and anything within this "is a string"
# single_string = ''
# double_string = ""

# How to Know It’s a String?
# If it looks like words or symbols and is wrapped in 
# quotes → it’s a string.

# If it doesn’t have quotes → Python thinks it’s a number, 
# a command, or a variable.



# Single quotes can hold strings
# single_quote = 'Tomisin does not understand string'
# single_quote = 'Tomisin does not understand string'
single_quote = "Flourish Field's academy" 


print("single quote =>", single_quote)
print("single quote =>", type(single_quote))


# This can break if there's an apostrophe inside
# The apostrophe in "Field's" ends the string too early
# That's why double quotes are better here
single_quote_error = "Flourish Field's academy"
print("single quote with apostrophe =>", single_quote_error)

# Double quotes can also hold strings (good when using apostrophes inside)
double_quote = "I am a double quote"
print("double quote =>", double_quote)

# Triple single quotes can hold multi-line strings (like a poem or a letter!)
single_multi_string = ''' 
A B C D E F
G H I J K L
M N O P Q R
'''
print("SINGLE multi-line string =>", single_multi_string)

# Triple double quotes do the same thing!
double_multi_string = """ 
J K L M N
O P Q R S
T U V W X
"""
print("DOUBLE multi-line string =>", double_multi_string)

# Numbers in quotes are still strings (they look like numbers, but are actually text!)
number_string = "40"
print("number_string =>", number_string)
print("number_string type =>", type(number_string))

# Numbers without quotes are real numbers (integers)
number_number = 40
print("number_number =>", number_number)
print("number_number type =>", type(number_number))

# You can combine strings using + or f-strings (string concatenation)
tomisin = "Tomisin"
peter = "Peter"
# Using + to join strings
message = "My name is " + tomisin + " and my surname is " + peter 
print("message (with +) =>", message)

# Using f-string (easier and cleaner!)

message_f = f"{tomisin} and {peter} are learning strings in Python!"
print("message (with f-string) =>", message_f)

# You can even mix in multi-line strings
fun_message = f"{double_multi_string}\n---\n{single_multi_string}"
print("fun message with multi-lines =>", fun_message)


#  1. What is an f-string?
# Think of it as a magic sentence that lets you plug in your variables easily.
name = input("Enter your name: ")
age = 11
print(f"My name is {name} and I am {age} years old.")

# 🔹 2. Compare with traditional concatenation:
# With + signs
print("My name is " + name + " and I am " + str(age) + " years old.")

# With f-string
# print(f"My name is {name} and I am {age} years old.")
# Explain: The f-string is shorter and easier to understand.

# 📘 Fun Real-World Analogy:
# Imagine your f-string is a sentence with blank spaces. 
# You just fill in the blanks with variables like a Mad Libs game!



# String,' 
# Combine three words into one sentence. 
name = "Alice"
location = "Wonderland"
activity = "exploring"

one_sentence = f"I am {name} and i am in {location} {activity}"
print(one_sentence)

# Make a string math that says "2 + 2 = 4" 
first_number = "2"
second_number = "2"
add_result = f"{first_number} + {second_number} = 4"
print(add_result)

# Create word and print the first letter using indexing. 
                #0123456
indexOfLetter = "Tomisin"
print(indexOfLetter[6])
print(len(indexOfLetter))



# Make a string repeat and repeat it 3 times. 



# Create story using several variables inside an f-string.
language = "Python"
level = "master"
name = "Tomisin"
storyboard = f"{name} is a {level} of {language} language"
print(storyboard)

# Use f-string to say "Hello, my name is [name]". 
name = "Tomisin"
print(f"my name is {name}")


# Combine firstName = "Tom" and lastName = "Jerry" into fullName. 
firstName = "Tomisin"
lastName = "Python"
fullName = f"{firstName} {lastName}"
print(fullName)