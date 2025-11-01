#  Think of a list like a lunchbox that can hold many items — rice, beans, meat, and water — all inside one box.
#  In Python, a list holds many values inside one variable — all stored neatly in order

# example
lunchbox = ["rice", "beans", "meat", "water"]

# 1. What Is a List?

# A list is a way to keep many values together inside one “box.”
# We use square brackets [ ] to make a list.

# Example:

# # A list of fruits
# fruits = ["apple", "banana", "mango"]

# # A list of numbers
# numbers = [1, 2, 3, 4, 5]

# 🧠 2. Why Do We Use Lists?

# Because sometimes we don’t just want one thing —
# we want to store many things together, like:

# names of friends

# scores in a game

# favorite colors

# items in a shopping cart

# Example:

# index      0        1        2
friends = ["Tomi", "Peace", "Joshua"]
print(friends)

# 🧰 3. How to Access Items in a List

# Each item in a list has a position number called an index.
# Python starts counting from 0.

# Example:

colors = ["red", "blue", "green"]
print(colors[0])  # red
print(colors[2])  # green
print(colors[1]) # blue

# 🪄 4. Changing Items in a List

# You can change an item by pointing to its index number.

# Example:
# Variable Name (lhs)     equals-to    value (rhs)
variableName             =            "Python for Peter and Tomisin"
# colors[2]                =            "brown"


colors = ["red", "blue", "green"]
# colors[1] = "yellow"
colors[1] = "indigo"
colors[2] = "brown"
print(colors)  # ['red', 'indigo', 'green']


# 🧩 5. Adding and Removing Items
fruits = ["apple", "orange", "watermelon"]
# Action	     Method	    Example	Result
# Add one item	.append()	fruits.append("orange")	Adds to the end
fruits.append("grape")
print(fruits)


# Add many items	.extend()	fruits.extend(["grape", "kiwi"])	Adds multiple
fruits.extend(["groundnut", "avocado"])
print(fruits)


# Add in a position	.insert(index, item)	fruits.insert(1, "pear")	Adds at position
fruits.insert(4, "pawpaw")
print(fruits)


# Remove one item	.remove()	fruits.remove("banana")	Removes by name
fruits.remove("grape")
print(fruits)

# Remove last item	.pop()	fruits.pop()	Removes last
fruits.pop()
print(fruits)

# Empty everything	.clear()	fruits.clear()	List becomes empty
# fruits.clear()
# print(fruits)

# 🧠 6. Other Useful Tricks
# Method	What it Does	Example	Output
# .sort()	Arranges items in order	fruits.sort()	Sorted list
fruits.sort()
print("fruits is sorted =>", fruits)

# .reverse()	Flips the list backwards	fruits.reverse()	Reversed
fruits.reverse()
print("fruits is reversed =>", fruits)

# len()	Counts how many items	len(fruits)	Number of items
print(len(fruits))

# "in"	Checks if an item exists	"apple" in fruits	True or False
print("pawpaw" in fruits)
print("fruits" in fruits)

# 🧮 7. Lists Can Hold Anything

# Lists can hold:

Strings = ["dog", "cat"]
print(Strings)


Integers = [1, 2, 3, 4, 5]    
print(Integers)

Booleans = [True, False]
print(Booleans)

mixedValues = ["cat", 20, True, {"name": "list"}]
print("mixedValues_list",mixedValues[3]["name"])
print(mixedValues)


# A list of students in class

# A list of favorite games

# Do a “What’s missing?” game by removing items from a list.

# 💻 9. Quick Practice Examples
animals = ["dog", "cat", "rabbit"]
print(animals[1])
animals.append("parrot")
print(animals)
animals.remove("cat")
print(animals)
print(len(animals))
print("rabbit" in animals)
