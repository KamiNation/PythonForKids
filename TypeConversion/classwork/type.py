# Imagine you have hot water but need it cold for your 
# drink you either cool it down or add ice to convert it.

# Just like that, sometimes in Python, you need to change 
# a value’s "type" to something else so it works in your code.

# Python Type Conversion Analogy
# Real Life	Python Code
# Hot water → Cold =>	float → int or str → int
# Cold water → Hot =>	int → float
# Ice cube → Water =>	str → float
# Water → Steam    =>	int → str

# Example Explanation for Kids:
# Let’s say someone types “5”
# inputNumber = input("Enter a number: ")
# addInputNumber = 10 + int(inputNumber)
# addFloatnumber = 10 + float(inputNumber)
# print("You entered:", inputNumber) 

# print("Adding 10 to your number gives:", addInputNumber)  # This will crash because inputNumber is a string,
# print("Adding 10.0 to your number gives:", addFloatnumber)  # This will crash because inputNumber is a string,

# but that’s a string, not a real number.
# You want to add that “5” to another number, like 10.
# But Python says: “Wait! You’re trying to add a word to a number! 
# That’s not allowed.”


# So, you convert it:
# age = "5"
# new_age = int(age) + 10
# print(new_age)  # Output: 15
# Now Python is happy! 🎉 You turned the word "5" into a 
# real number using int()!

# 🔟 Type Conversion Challenge Questions for Kids
# 🧊🔥 (Hot & Cold Water Style)

# Hot to Cold Water!
# age = "12"
# ➤ What do you need to do so you can add age to a number like 3?

# Real Action!
# Convert "100" (a string) into a number and add 50 to it.
# ➤ What will the output be?



# Cold to Hot Water!
# score = 10
# ➤ Convert it into a string so you can join it with:
# print("Your score is " + ?)


# Ice to Water!
# Convert the string "3.14" into a number with decimal.

# ➤ Which function do you use?
# Which One Works?
# Which of these will crash your code?

 
# a = int("4")
# b = float("5.0")
# c = int("hello")
# What Will Print?

# number = "7"
# print(int(number) + 3)
# ➤ What will this output be?

# Fix the error!
# age = "10"
# print("Next year, you will be " + age + 1)


# ➤ This will crash! How would you fix it?
# What is the Type After Conversion?
# val = str(9.8)
# ➤ What is the type of val now?


# Turn Water into Steam!
# ➤ Write a line of code that turns number 50 into a string and prints:
# "Your score is 50"

# Can You Convert This?
# data = "True"
# ➤ Can you convert this string into a real boolean value in Python?
# (Hint: Try bool(data) — what does it return?)


# stringNumber = input("Enter a number: ")
# addNumber = 8 + int(stringNumber)
# addNumber = 8 + stringNumber

# print("addNumber =>", addNumber)
# This will crash because you can't add a string and an integer directly.


# You have the number 25 as an integer. Change it into a string and join it with the word "years".
# number as an integer
number25 = 25
print("Number25 has an integer =>", type(number25))

# converting number25 to a string
changedNumber = str(number25)
print("changeNumber has a string =>", type(changedNumber))

# joining the string with the word "years"
methodOne = "I am " + changedNumber + " years old."
print("Method One =>", methodOne)

methodTwo = f"I am {changedNumber} years old"
print("Method Two =>", methodTwo)


unchangedNumber = "3.4" # string value, 3 to 3 integer and not 3.4 string integer to 3.4 integer
print("unchangedNumber has a string =>", type(unchangedNumber))
# converting unchangedNumber to a float then to an integer
# mychangedNumber = int(unchangedNumber)  # This will crash because "3.4" is not an integer string
notmychangedNumber = float(unchangedNumber)  # This will convert to float but not to int
# So we first convert to float, then to int to avoid crashing
changedNumber = int(float(unchangedNumber))
print("changedNumber has an integer =>", type(changedNumber))
print("changedNumber =>", changedNumber)
print("notmychangedNumber has a float =>", type(notmychangedNumber))
print("notmychangedNumber =>", notmychangedNumber)
# print("my changedNumber has an integer =>", type(mychangedNumber))
# print("my changedNumber =>", mychangedNumber)