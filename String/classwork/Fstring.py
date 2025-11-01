# You can combine strings using + or f-strings (string concatenation)

topic = "string"
stringAddition = " + to join strings"
fStringAddition = "Use f-string (easier and cleaner!)"
message = "We are learing " + topic + " in python and we use " + stringAddition + " or " + fStringAddition
f_message = f"We're learning {topic} in python and we use {stringAddition} or {fStringAddition}"
print(message)
print(f_message)

mathgrade = 93
englishgrade = 97
f_message = f"My math grade is {mathgrade} and my english grade is {englishgrade}"
print(f_message)

color = "blue"
f_message2 = f"Wow! {color} is my favourite color too!"
print(f_message2)

pet = "Jake"
f_message3 = f"My pet's name is {pet}"
print(f_message3)