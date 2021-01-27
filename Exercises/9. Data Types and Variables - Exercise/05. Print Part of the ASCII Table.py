# 5.	Print Part of the ASCII Table
# Find online more information about ASCII (American Standard Code for Information Interchange) and write a
# program that prints part of the ASCII table of characters on the console.  On the first line of input you will
# receive the char index you should start with and on the second line - the index of the last character you
# should print.


range_start = int(input())
range_end = int(input())
range_end += 1

for i in range(range_start, range_end):
    print(chr(i), end=" ")