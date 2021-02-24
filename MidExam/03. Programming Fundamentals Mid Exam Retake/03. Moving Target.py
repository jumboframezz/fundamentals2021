# You are at the shooting gallery again and you need a program that helps you keep track of moving targets. On the
# first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you
# will start receiving commands for manipulating the targets, until the "End" command. The commands are the following:
#   •	Shoot {index} {power}
#           o	Shoot the target at the index, if it exists by reducing its value by the given
#               power (integer value).A target is considered shot when its value reaches 0.
#           o	Remove the target, if it is shot.
#   •	Add {index} {value}
#           o	Insert a target with the received value at the received index, if it exist. If not, print:
#                   "Invalid placement!"
#   •	Strike {index} {radius}
#           o	Remove the target at the given index and the ones before and after it depending on the radius,
#               if such exist. If any of the indices in the range is invalid print:
#                   "Strike missed!" and skip this command.
#  Example:  Strike 2 2
# 	{radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
#   •	End
#          o	Print the sequence with targets in the following format:
#                   {target1}|{target2}…|{targetn}
def shoot(s_idx, s_pwr):
    if 0 <= s_idx < len(line):
        line[s_idx] -= s_pwr
        if line[s_idx] <= 0:
            line.pop(s_idx)
    return line


def add_target(add_idx, add_pwr):
    if 0 <= add_idx < len(line):
        line.insert(add_idx, add_pwr)
    else:
        print("Invalid placement!")
    return line


def strike(st_index, st_radius):
    if st_index - st_radius < 0 or st_index + st_radius >= len(line):
        print("Strike missed!")
        return line

    start_index = st_index - st_radius
    end_index = index + st_radius
    first = line[0:start_index]
    second = line[end_index + 1:]
    first.extend(second)

    return first


line = [int(_) for _ in input().split()]
command = input()
while command != "End":
    cmd, index, val = command.split()
    index = int(index)
    val = int(val)
    if cmd == "Shoot":
        line = shoot(index, val)
    elif cmd == "Add":
        line = add_target(index, val)
    elif cmd == "Strike":
        line = strike(index, val)
    command = input()

print("|".join([str(_) for _ in line]))
