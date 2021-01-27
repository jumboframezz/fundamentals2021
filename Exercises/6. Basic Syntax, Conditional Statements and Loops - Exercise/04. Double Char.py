# 4.	Double Char
# Given a string, you have to print a string in which each character (case-sensitive) is repeated.
# Examples
# Input	Output
# Hello World	HHeelllloo  WWoorrlldd
# 1234!	11223344!!

entry = input()
for i in entry:
    print(i*2, end="")