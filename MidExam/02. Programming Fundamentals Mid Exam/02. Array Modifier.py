# You are given an array with integers. Write a program to modify the elements after receive the
# commands “swap”, “multiply” or “decrease”.
#   •	“swap {index1} {index2}” take two elements and swap their places.
#   •	“multiply {index1} {index2}” take element at the 1st index and multiply it with element at 2nd index.
#        Save the product at the 1st index.
#   •	“decrease” decreases all elements in the array with 1.
def swap(sw_idx1, sw_idx2):
    global line
    line[sw_idx1], line[sw_idx2] = line[sw_idx2], line[sw_idx1]
    return line


def multiply(mul_idx1, mul_idx2):
    global line
    line[mul_idx1] = line[mul_idx1] * line[mul_idx2]
    return line


line = [int(_) for _ in input().split()]
command = input()
while command != "end":
    cmd = command.split()
    if len(cmd) > 1:
        cmd[1] = int(cmd[1])
        cmd[2] = int(cmd[2])
    if cmd[0] == "swap":
        swap(cmd[1], cmd[2])
    elif cmd[0] == "multiply":
        multiply(cmd[1], cmd[2])
    elif cmd[0] == "decrease":
        line = [_ - 1 for _ in line]
    command = input()


print(", ".join([str(_) for _ in line]))
