# Write a program that counts all characters in a string except for space (' ').
# Print all the occurrences in the following format:
# {char} -> {occurrences}

line = input()
letters = {}
for letter in filter(lambda x: x != " ",  line):
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1

for letter in letters:
    print(f"{letter} -> {letters[letter]}")
