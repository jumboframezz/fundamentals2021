# *Snowballs
# Tony and Andi love playing in the snow and having snowball fights, but they always argue which makes the best
# snowballs. They have decided to involve you in their fray, by making you write a program, which calculates
# snowball data, and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# For each snowball you will receive 3 input lines:
#   •	On the first line you will get the snowball_snow – an integer.
#   •	On the second line you will get the snowball_time – an integer.
#   •	On the third line you will get the snowball_quality – an integer.
# For each snowball you must calculate its snowball_value by the following formula:
#       (snowball_snow / snowball_time) ** snowball_quality
# At the end you must print the highest calculated snowball_value.
# Input
#   •	On the first input line you will receive N – the number of snowballs.
#   •	On the next N * 3 input lines you will be receiving data about snowballs.
# Output
#   •	As output, you must print the highest calculated snowball_value, by the formula, specified above.
#   •	The output format is:
#       {snowball_snow} : {snowball_time} = {snowball_value} ({snowball_quality})
# Constraints
#   •	The number of snowballs (N) will be an integer in range [0, 100].
#   •	The snowball_snow is an integer in range [0, 1000].
#   •	The snowball_time is an integer in range [1, 500].
#   •	The snowball_quality is an integer in range [0, 100].
import sys
best_snowball_value = -sys.maxsize
best_snowball_snow = -sys.maxsize
best_snowball_time = -sys.maxsize
best_snowball_quality = -sys.maxsize

n = int(input())

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
print(f"{best_snowball_snow} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})")
