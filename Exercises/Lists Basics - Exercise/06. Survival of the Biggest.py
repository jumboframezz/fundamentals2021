# 6.	Survival of the Biggest
# Write a program that receives a list of integer numbers and a number n. The number n represents the amount of
# numbers to remove from the list. You should remove the smallest ones.
# Input
#   On the first line you will receive a string (numbers separated by a space), on the second line you
#   will receive a number n (count of numbers to remove).
# Output
# Print all the numbers that are left in the list.

line = [int(_) for _ in input().split()]
numbers = int(input())
sorted_line = []
sorted_line.extend(line)
sorted_line.sort()
sorted_line = sorted_line[:numbers]

for el in sorted_line:
    line.remove(el)
print(line)