#  2. Operator Precedence
#  Idea for Kids

# Operator precedence means who goes first when Python sees more 
# than one operation.
# Just like in class, if your teacher says, 
# “Do brackets first, then multiply, 
# then add,” that’s the rule Python follows too!

# 🧩 Order of Operation (BODMAS, Bracket first, 
# Division, Multiplication, Addition, Subtraction)

# Step	What to Do First	            Example
#   1	Parentheses ()	                (2 + 3) * 4 → 20
#   2	   Exponents **	                2 ** 3 * 4 → 32
#   3	Multiplication/Division	        10 / 2 * 5 → 25
#   4	Addition/Subtraction	        10 - 2 + 3 → 11


# # 💻 Example
result = 2 + 3 * 4
print(result)   # 14 (because 3*4 happens first)

result2 = (2 + 3) * 4
print(result2)  # 20 (because () happens first)

# 🧠 Left Associativity

# When two operators have the same power or level,
# Python reads them from left to right 
# like reading a sentence in English!

# 📘 Example:

# print(10 - 3 + 2)


# 👉 Python starts from left to right:
# 10 - 3 = 7, then 7 + 2 = 9

# So the answer is 9, not 5.
# That’s what we mean by left associativity;
# Python goes from left to right when operators are equal friends. 👬

# 💻 Examples
# result = 2 + 3 * 4
# print(result)   # 14 (because 3*4 happens first)

# result2 = (2 + 3) * 4
# print(result2)  # 20 (because () happens first)

# result3 = 10 - 3 + 2
# print(result3)  # 9 (because Python goes left to right)

# 🎯 Mini Challenges (4 Examples)

# What’s the output of 2 + 3 * 5?

# Try 10 - 3 + 2 * 2.

# Add brackets to 5 + 4 * 2 so that the result becomes 18.

# Predict what happens in 8 / 2 * 4 — remember left-to-right!

# 🎯 Mini Challenges (3 examples)

# What’s the output of 2 + 3 * 5?
print(2 + 3 * 5)  # 17

# Try 10 - 3 + 2 * 2.
print(10 - 3 + 2 * 2)  # 11

# Add brackets to 5 + 4 * 2 so that the result becomes 18.
print((5 + 4) * 2)  # 18
print(5 + 4 * 2)  # 18
