# 2.	Drink Something
# Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
# Make a program that receives an age, and returns what they drink.
# Rules:
# Kids under 14 years old.
# Teens under 18 years old.
# Young adults under 21 years old.
# Adults above 21.
# Note: All the values except the last one are inclusive!
# Examples
# Input	Output
# 13	drink toddy
# 17	drink coke
# 21	drink beer
# 30	drink whisky


age = int(input())
drink = ""
if age <= 14:  # Kids
    drink = "toddy"
elif 13 < age <= 18:  # Teens
    drink = "coke"
elif 18 < age <= 21:  # Young adult
    drink = "beer"
elif age > 21:
    drink = "whisky"
print(f"drink {drink}")
