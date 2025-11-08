# . If Statements (Decision Making)
# 💡 What is an If Statement?

# An if statement lets Python make decisions — it checks a condition and then decides what to do next.

# Think of it like real life:

# “If it’s raining, take an umbrella.
# Otherwise, wear your sunglasses.”


# Comparison Operators (Used with if)
# Symbol	    Meaning	                    Example	Result
# ==	        Equal to	                5 == 5	True
# !=	        Not equal to	            5 != 3	True
# >	            Greater than	            10 > 5	True
# <	            Less than	                4 < 8	True
# >=	        Greater than or equal	    7 >= 7	True
# <=	        Less than or equal	        6 <= 9	True

# So, Python uses if, elif, and else to decide what happens based on conditions.

# Basic If Statement
age = 18

if age >= 18:
    print("You're an adult")

# if age >= 18:
#     print("You are an adult.")


# 👉 The code inside runs only if the condition (age >= 18) is True.

# 🧱 If-Else Statement
age = 16
 
#    16 >= 18 is False, so the else part runs.
if age >= 18: # true
    print("You are an adult.")
else:
    print("You are a teenager.")


# If the condition is False, Python skips the if part and runs the else block.

# 🧱 If-Elif-Else (Multiple Choices)
score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent!")
elif score >= 70: #elif; else if
    print("Good job!")
else:
    print("Keep trying!")


# 👉 Python checks conditions from top to bottom.
# Once one condition is True, it ignores the rest.

# Compare this to a traffic light:

# If light is red → stop

# Else if light is yellow → slow down

# Else → go
