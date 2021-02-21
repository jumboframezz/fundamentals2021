# Input
# You will receive an initial list with groceries separated by "!".
# After that you will be receiving 4 types of commands, until you receive "Go Shopping!"
#   •	Urgent {item} - add the item at the start of the list.  If the item already exists, skip this command.
#   •	Unnecessary {item} - remove the item with the given name, only if it exists in the list. Otherwise skip
#       this command.
#   •	Correct {oldItem} {newItem} – if the item with the given old name exists, change its name with the new one.
#       If it doesn't exist, skip this command.
#   •	Rearrange {item} - if the grocery exists in the list, remove it from its current position and add it at
#       the end of the list.
# Constraints
#   •	There won`t be any duplicate items in the initial list
# Output
# Print the list with all the groceries, joined by ", ".
#   •	"{firstGrocery}, {secondGrocery}, …{nthGrocery}"
def urgent(urg_item):
    if urg_item not in line:
        line.insert(0, urg_item)
    return line


def unnecessary(un_item):
    if un_item in line:
        line.remove(un_item)
    return line


def correct(cor_old, cor_new):

    if cor_old in line:
        idx = line.index(cor_old)
        line[idx] = cor_new
    return line

def rearrange (re_item):
    if re_item in line:
        idx = line.index(re_item)
        _ = line.pop(idx)
        line.append(_)
    return line


line = input().split("!")
entry = input()
while entry != "Go Shopping!":
    command = entry.split()
    if command[0] == "Urgent":
        line = urgent(command[1])
    elif command[0] == "Unnecessary":
        line = unnecessary(command[1])
    elif command[0] == "Rearrange":
        line = rearrange(command[1])
    elif command[0] == "Correct":
        line = correct(command[1], command[2])
    entry = input()

print(", ".join([_ for _ in line]))
