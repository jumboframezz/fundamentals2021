# Write a program that receives two numbers (factor and count) and creates a list with length of the given count and
# contains only elements that are multiples of the given factor.

factor = int(input())
count = int(input())
val = 0
result = []
for i in range(count):
    val += factor
    result.append(val)

print(result)
