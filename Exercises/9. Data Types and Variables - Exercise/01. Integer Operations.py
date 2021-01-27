# 1.	Integer Operations
# Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and multiply the
# result by the fourth number. Print the result.
#
# Input	Output
# 10
# 20
# 3
# 3	    30


first = int(input())
second = int(input())
third = int(input())
forth = int(input())

res = ((first + second) // third) * forth
print(res)