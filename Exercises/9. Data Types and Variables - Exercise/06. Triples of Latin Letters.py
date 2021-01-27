# 6.	Triples of Latin Letters
# Write a program to read an integer n and print all triples of the first n small Latin letters, ordered
# alphabetically:
# Examples
# Input	Output
# 3
# aaa
# aab
# aac
# aba
# abb
# ...

n = int(input())

start_range = ord('a')
end_range = start_range + n

for i in range(start_range, end_range):
    for ii in range(start_range, end_range):
        for iii in range(start_range, end_range):
            print(f"{chr(i)}{chr(ii)}{chr(iii)}")
