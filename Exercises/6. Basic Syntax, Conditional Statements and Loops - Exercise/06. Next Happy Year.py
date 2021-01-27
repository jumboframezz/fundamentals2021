# 6.	Next Happy Year
# You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct
# digits, (e.g) 2018. Write a program that receives an integer number and finds the next happy year.
# Examples
# Input	Output
# 8989	9012
# 1001	1023

def check_year(yr):
    if len(yr) == len(set(yr)):
        return True
    return False


year = input()
curr_year = int(year) + 1
found = False
while not found:
    str_year = str(curr_year)
    if check_year(str_year):
        found = True
    else:
        curr_year += 1

print(curr_year)




