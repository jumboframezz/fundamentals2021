# 3.	Legendary Farming
# You've done all the work and the last thing left to accomplish is to own a legendary item. However, it's a tedious
# process and it requires quite a bit of farming. Anyway, you are not too pretentious – any legendary item will do.
# The possible items are:
#   •	Shadowmourne – requires 250 Shards;
#   •	Valanyr – requires 250 Fragments;
#   •	Dragonwrath – requires 250 Motes;
#   Shards, Fragments and Motes are the key materials and everything else is junk. You will be given lines of input,
#   in the format:
#       2 motes 3 ores 15 stones
# Keep track of the key materials - the first one that reaches the 250 mark, wins the race. At that point you have to
# print that the corresponding legendary item is obtained. Then, print the remaining shards, fragments, motes,
# ordered by quantity in descending order, then by name in ascending order, each on a new line. Finally, print the
# collected junk items in alphabetical order.
# Input
#   •	Each line comes in the following format: {quantity} {material} {quantity} {material} … {quantity} {material}
# Output
#   •	On the first line, print the obtained item in the format: {Legendary item} obtained!
#   •	On the next three lines, print the remaining key materials in descending order by quantity
#       o	If two key materials have the same quantity, print them in alphabetical order
#   •	On the final several lines, print the junk items in alphabetical order
#       o	All materials are printed in format {material}: {quantity}
#       o	The output should be lowercase, except for the first letter of the legendary

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = {"Shadowmourne": 0, "Valanyr": 0, "Dragonwrath": 0}
junk_items = {}
found = False
while True:
    line = input().split()
    for entry in range(0, len(line), 2):
        qty = int(line[entry])
        material = line[entry + 1].lower()
        if material in key_materials:
            if material == "shards":
                legendary_items["Shadowmourne"] += qty
            elif material == "fragments":
                legendary_items["Valanyr"] += qty
            elif material == "motes":
                legendary_items["Dragonwrath"] += qty
            key_materials[material] += qty

        else:
            if material not in junk_items:
                junk_items[material] = qty
            else:
                junk_items[material] += qty
    for item in legendary_items.items():
        if item[1] >= 250:
            print(f"{item[0]} obtained!")
            legendary_items[item[0]] -= 250
            found = True
            break
    if found:
        break


for key, value in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{key}: {value}")


for key, value in sorted(junk_items.items()):
    print(f"{key}: {value}")
