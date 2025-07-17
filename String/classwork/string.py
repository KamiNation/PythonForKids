# What Is a String in Python?
# A string is like a sentence or word wrapped in quotes.


# Think of it as a gift box for words, letters, numbers, 
# emojis anything you want to say!
# As long as it’s inside quotation marks (" " or ' '), 
# Python treats it as a string.


# we use the "", and anything within the "is a string"
# single_string = ''
# double_string = ""

# How to Know It’s a String?
# If it looks like words or symbols and is wrapped in 
# quotes → it’s a string.

# If it doesn’t have quotes → Python thinks it’s a number, 
# a command, or a variable.

# 🧠 Easy Analogy:
# “A string is anything you’d say out loud or write in a 
# text message — wrapped in quotes!”





single_quote = 'I am a single quote'
print("single quote =>", single_quote)



single_quote_error = "Flourish Field's academy"
print("single quote error=>", single_quote_error)

double_quote = "I am a double quote"
print("double quote =>", double_quote)

single_multi_string = ''' 
A B C D E F
G H I J K L
M N O P Q R
'''
print("SINGLE_multi_string =>", single_multi_string)

double_multi_string = """ 
J K L M N
O P Q R S
T U V W X
"""
print("DOUBLE_multi_string =>", double_multi_string)

number_string = "40"
print("number_string =>", number_string)
print("number_string =>", type(number_string))

number_number = 40

print("number_number =>", number_number)
print("number_number =>", type(number_number))

tomisin = "Tomisin "
peter = "Peter"
# message = tomisin + " and " + peter + " are learning string in python"
message =  f"{tomisin} and {peter} are learning string in python"
message0ne = f"{double_multi_string} and {single_multi_string}"
print("message =>", message)
print("message =>", message0ne)
