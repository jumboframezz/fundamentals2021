# Write a program to read a sequence of integers and find and print the top 5 numbers that are greater than the
# average value in the sequence, sorted in descending order.
# Input
# Read from the console a single line holding space separated number.
# Output
# Print the above described numbers on a single line, space separated. If less than 5 numbers hold the above
# mentioned property, print less than 5 numbers. Print “No” if no numbers hold the above property.
# Constraints
# All input numbers are integers in range [-1 000 000 … 1 000 000]. The count of numbers is in range [1…10 000].


line = [int(_) for _ in input().split()]

average = sum(line) / len(line)

result = filter(lambda x:  x > average, sorted([_ for _ in line if _ >= average], reverse=True))
result = list(result)
if len(result) == 0:
    print("No")
    exit(0)

if len(result) <= 5:
    print(" ".join([str(_) for _ in sorted(result, reverse=True)]))
elif len(result) >= 6:
    print(" ".join([str(_) for _ in sorted(result[:5], reverse=True)]))



