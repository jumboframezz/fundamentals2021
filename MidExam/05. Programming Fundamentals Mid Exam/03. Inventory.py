# Input / Constraints
# You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until
# receiving "Craft!" you will be receiving different commands.
# Commands (split by " - "):
# •	"Collect - {item}" – Receiving this command, you should add the given item in your inventory. If the item
# already exists, you should skip this line.
# •	"Drop - {item}" – You should remove the item from your inventory, if it exists.
# •	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists, if so, add the new item after
# the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
# Output
# After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).
def collect(cl_item):
    if cl_item in line:
        return line
    else:
        line.append(cl_item)
    return line


def drop(dr_item):
    if dr_item in line:
        line.remove(dr_item)
    return line


def combine(cm_item):
    old_item, new_item = cm_item.split(":")
    if old_item in line:
        idx = line.index(old_item)
        line.insert(idx+1, new_item)
    return line


def renew(rn_item):
    if rn_item in line:
        idx = line.index(rn_item)
        sw = line.pop(idx)
        line.append(sw)
    return line



line = input().split(", ")
command = input()
while command != "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        line = collect(item)
    elif action == "Drop":
        line = drop(item)
    elif action == "Combine Items":
        line = combine(item)
    elif action == "Renew":
        line = renew(item)
    command = input()

print(", ".join([_ for _ in line]))
