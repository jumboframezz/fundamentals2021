# Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros
# and moves them to the back without messing up the other elements. Print the resulting integer list
# Example
# Input	                    Output
# 1, 0, 1, 2, 0, 1, 3	    [1, 1, 2, 1, 3, 0, 0]

line = [int(_) for _ in input().split(", ")]
zeros = []
result = []
for item in line:
    if item == 0:
        zeros.append(item)
    else:
        result.append(item)
result.extend(zeros)
print(result)


