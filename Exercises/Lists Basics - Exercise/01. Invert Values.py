# Write a program that receives a single string containing numbers separated by a single space. Print a list
# containing the opposite of each number.


line = [int(_) * -1 for _ in input().split()]
print(line)
