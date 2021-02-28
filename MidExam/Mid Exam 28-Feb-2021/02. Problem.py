def blacklist(bl_name):
    global friends
    global blacklisted
    if bl_name in friends:
        idx = friends.index(bl_name)
        friends[idx] = "Blacklisted"
        blacklisted += 1
        print(f"{bl_name} was blacklisted.")
    else:
        print(f"{bl_name} was not found.")
    return friends


def error(e_index):
    global friends
    global lost
    if friends[e_index] != "Blacklisted" and friends[e_index] != "Lost":
        print(f"{friends[e_index]} was lost due to an error.")
        friends[e_index] = "Lost"
        lost += 1
    return friends


def change(ch_index, ch_name):
    global friends
    if 0 <= ch_index < len(friends):
        print(f"{friends[ch_index]} changed his username to {ch_name}. ")
        friends[ch_index] = ch_name
    return friends


friends = input().split(", ")
blacklisted = 0
lost = 0
cmd = input()
while cmd != "Report":
    cmd = cmd.split()
    if cmd[0] == "Blacklist":
        friends = blacklist(cmd[1])
    elif cmd[0] == "Error":
        friends = error(int(cmd[1]))
    elif cmd[0] == "Change":
        friends = change(int(cmd[1]), cmd[2])
    cmd = input()

print(f"Blacklisted names: {blacklisted} ")
print(f"Lost names: {lost} ")
print(" ".join([_ for _ in friends]))
