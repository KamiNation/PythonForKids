# dict	A pair of label and value	{"hero": "Spiderman"}

# personalData = ["tomisin", 11, "5'4"]
# personalDataDict = {"name": "tomisin", "age": 11, "height": "5'4"}

# How to get information

# print(personalDataDict["name"])
# print(personalDataDict.get("age"))

# 🧠 Topic: Dictionary (dict) in Python
# 💡 Analogy:

# Think of a dictionary in Python like a real-life dictionary or a school record book.

# Just like:

# 📘 In your dictionary, every word has a meaning —
# in Python, every key has a value.

# Example:

# "name" → "Tomi"
# "age" → 11
# "school" → "Flourish Field"

# 🧩 1. What Is a Dictionary?

# A dictionary is used to store information in pairs —
# something called a key and its value.

# Syntax:


# 🔍 2. What Are Keys and Values?
# Term	Meaning	Example
# Key	The label or question	"name", "age"
# Value	The answer to that label	"Tomi", 11

# In the dictionary above:

# "name" → is a key

# "Tomi" → is its value

# 🧠 3. How to Get Information (Accessing Values)

# You can get a value by calling its key inside square brackets or using .get().

# Example:

# print(student["name"])     # Tomi
# print(student.get("age"))  # 11

# ✍️ 4. How to Change a Value

# You can update any value using its key.

student = {
    "name": "Tomi",
    "age": 11,
    "school": "Flourish Field Academy"
}
# Example:

# student["age"] = 12
# print(student)

# Variable Name (lhs)     equals-to    value (rhs)
# variableName = "Python for Peter and Tomisin"
student["name"] = "Tomisin and Israel"
print(student)

# ➕ 5. How to Add a New Key-Value Pair

# You can add new information easily:

# student["grade"] = "Primary 6"
# print(student)
student["programmingLanguage"] = "Python"
print(student)

# ❌ 6. How to Remove Something

# Use .pop() or del to remove a key-value pair.

# Example:

# student.pop("school")
student.pop("name")
print(student)
# # or
# del student["age"]
del student["programmingLanguage"]
print(student)


# 🧩 7. How to See All Keys or Values

# You can look at all the keys, values, or both!

# Example:

# print(student.keys())    # dict_keys(['name', 'age', 'grade'])
print("student keys =>",student.keys())
# print(student.values())  # dict_values(['Tomi', 12, 'Primary 6'])
print("student values =>", student.values())
# print(student.items())   # dict_items([('name', 'Tomi'), ('age', 12), ('grade', 'Primary 6')])
print("student items =>", student.items())

# 🔁 8. Looping Through a Dictionary

# You can go through each pair one by one:

# Example:

# for key, value in student.items():
#     print(key, "=>", value)


# Output:

# name => Tomi
# age => 12
# grade => Primary 6

# 🧰 9. Dictionary Inside a Dictionary (Bonus)

# You can also put a dictionary inside another one!

# Example:

# students = {
#     "Tomi": {"age": 11, "grade": "5"},
#     "Peace": {"age": 12, "grade": "6"}
# }

# 🧑‍🏫 10. Teaching Tips

# To make it fun:

# Tell students: “Think of your school report card — it has your name, age, and scores. That’s a dictionary!”

# Let them create their own dictionary with their name, age, and favorite food.

# Play “find the value” — you say a key, they tell you the value in code.

# 💻 Mini Example
# myself = {
#     "name": "Joshua",
#     "age": 11,
#     "hobby": "Drawing"
# }

# print("My name is", myself["name"])
# print("I am", myself["age"], "years old.")
# print("I love", myself["hobby"])
