# Problem 2. Shoot for the Win
# Write a program that helps you keep track of your shot targets. You will receive a sequence with integers,
# separated by single space, representing targets and their value. Afterwards, you will be receiving indices
# until the "End" command is given and you need to print the targets and the count of shot targets.
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Everytime you shoot a target, its value becomes -1 and it is considered shot. Along with that you also need to:
#   •	Reduce all the other targets, which have greater values than your current target, with its value.
#   •	All the targets, which have less than or equal value to the shot target, you need to increase with its value.
# Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target,
# which is considered shot.
# When you receive the "End" command, print the targets in their current state and the count of shot
# targets in the following format:
#               "Shot targets: {count} -> {target1} {target2}… {targetn}"
# Input / Constraints
#   •	On the first line of input you will receive a sequence of integers, separated by a single
#       space – the targets sequence.
#   •	On the next lines, until the "End" command you be receiving integers each on a single
#       line – the index of the target to be shot.
# Output
# •	The format of the output is described above in the problem description.

targets = [int(_) for _ in input().split()]
shot_count = 0
index = input()
while index != "End":
    index = int(index)
    if 0 <= index < len(targets):
        if targets[index] != -1:
            old_value = targets[index]
            targets[index] = -1
            shot_count += 1
            for idx in range(len(targets)):
                if targets[idx] > old_value:
                    targets[idx] -= old_value
                elif targets[idx] <= old_value and targets[idx] != -1:
                    targets[idx] += old_value

    index = input()

print(f"Shot targets: {shot_count} -> {' '.join([str(_) for _ in targets])}")
