# 10. *Array Manipulator
# Trifon has finally become a junior developer and has received his first task. It's about manipulating an array of
# integers. He is not quite happy about it, since he hates manipulating arrays. They are going to pay him a lot of
# money, though, and he is willing to give somebody half of it if to help him do his job. You, on the other hand,
# love arrays (and money) so you decide to try your luck.
# The array may be manipulated by one of the following commands
#   •	exchange {index} – splits the array after the given index, and exchanges the places of the two resulting
#       sub-arrays. E.g. [1, 2, 3, 4, 5] -> exchange 2 -> result: [4, 5, 1, 2, 3]
#           o	If the index is outside the boundaries of the array, print "Invalid index"
#   •	max even/odd– returns the INDEX of the max even/odd element -> [1, 4, 8, 2, 3] -> max odd -> print 4
#   •	min even/odd – returns the INDEX of the min even/odd element -> [1, 4, 8, 2, 3] -> min even > print 3
#           o	If there are two or more equal min/max elements, return the index of the rightmost one
#           o	If a min/max even/odd element cannot be found, print "No matches"
#   •	first {count} even/odd– returns the first {count} elements -> [1, 8, 2, 3] -> first 2 even -> print [8, 2]
#   •	last {count} even/odd – returns the last {count} elements -> [1, 8, 2, 3] -> last 2 odd -> print [1, 3]
#           o	If the count is greater than the array length, print "Invalid count"
#           o	If there are not enough elements to satisfy the count, print as many as you can. If there
#               are zero even/odd elements, print an empty array "[]"
#   •	end – stop taking input and print the final state of the array
# Input
#   •	The input data should be read from the console.
#   •	On the first line, the initial array is received as a line of integers, separated by a single space
#   •	On the next lines, until the command "end" is received, you will receive the array manipulation commands
#   •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
#   •	The output should be printed on the console.
#   •	On a separate line, print the output of the corresponding command
#   •	On the last line, print the final array in square brackets with its elements separated by a comma and a space
#   •	See the examples below to get a better understanding of your task
# Constraints
#   •	The number of input lines will be in the range [2 … 50].
#   •	The array elements will be integers in the range [0 … 1000].
#   •	The number of elements will be in the range [1 .. 50]
#   •	The split index will be an integer in the range [-231 … 231 – 1]
#   •	first/last count will be an integer in the range [1 … 231 – 1]
#   •	There will not be redundant whitespace anywhere in the input
#   •	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.
import sys


def exchange(arr, index):
    first = arr[index + 1:]
    second = arr[:index + 1]
    return first + second


# find_max
def find_max(arr):
    max_odd = -sys.maxsize
    max_even = -sys.maxsize
    index_odd = []
    index_even = []
    r = []
    for index in range(len(arr)):
        if arr[index] >= max_odd and arr[index] % 2 != 0:
            max_odd = arr[index]
            index_odd.append(index)
        elif arr[index] >= max_even and arr[index] % 2 == 0:
            max_even = arr[index]
            index_even.append(index)

    if len(index_odd) > 0:
        r.append(index_odd[-1])
    else:
        r.append(-1)
    if len(index_even) > 0:
        r.append(index_even[-1])
    else:
        r.append(-1)
    return r


# find_min
def find_min(arr):
    min_odd = sys.maxsize
    min_even = sys.maxsize
    index_odd = []
    index_even = []
    r = []
    for index in range(len(arr)):
        if arr[index] <= min_odd and arr[index] % 2 != 0:
            min_odd = arr[index]
            index_odd.append(index)
        elif arr[index] <= min_even and arr[index] % 2 == 0:
            min_even = arr[index]
            index_even.append(index)

    if len(index_odd) > 0:
        r.append(index_odd[-1])
    else:
        r.append(-1)
    if len(index_even) > 0:
        r.append(index_even[-1])
    else:
        r.append(-1)
    return r


def max_odd_or_even(arr, parity):
    max_indexes = find_max(arr)
    print(f"max_indexes: {max_indexes}")
    if parity == "even":
        if max_indexes[1] >= 0:
            print(max_indexes[1])
        else:
            print("No matches")
    else:
        if max_indexes[0] >= 0:
            print(max_indexes[0])
        else:
            print("No matches")


def min_odd_or_even(arr, parity):
    min_indexes = find_min(arr)
    print(f"min_indexes: {min_indexes}")
    if parity == "even":
        if min_indexes[1] >= 0:
            print(min_indexes[1])
        else:
            print("No matches")
    else:
        if min_indexes[0] >= 0:
            print(min_indexes[0])
        else:
            print("No matches")


def geteven(arr):
    r = [item for item in arr if item % 2 == 0]
    return r

def getodd(arr):
    r = [item for item in arr if item % 2 != 0]
    return r


line = [int(_) for _ in input().split()]
#line = [1, 4, 8, 2, 3]


param1 = ""
param2 = ""
command_type = ""
print(line)
command = input()
debug = False
while command != "end":
    list_line = command.split()
    if len(list_line) == 3:
        command_type, param1, param2 = [_ for _ in list_line]
    elif len(list_line) == 2:
        command_type, param1 = [_ for _ in list_line]
        param2 = ""  # Just to clean up
    if debug:
        print(f"command_type: {command_type} param1: {param1} param2: {param2}")

    if command_type == "exchange":
        if param1 >= len(line):
            print("Invalid index")
        else:
            line = exchange(line, int(param1))

    if command_type == "max":
        max_odd_or_even(line, param1)

    if command_type == "min":
        min_odd_or_even(line, param1)
    if command_type == "first":
        #  first {count} even/odd
        if param2 == "odd":
            if int(param1) > len(line):
                print("Invalid count")
            r = getodd(line)
            line_len = int(param1)
            print(f"r: {r}  line_len: {line_len}")
            print(r[:line_len])
        pass
    if command_type == "last":
        pass

    command = input()