# You really like big numbers, so you always find a way to form one from numbers given to you
# You will receive a single line containing numbers separated by a single space. Sort and reverse the numbers
# then return them as a string.

line = input().split()
line.sort(reverse=True)
print("".join([_ for _ in line]))
