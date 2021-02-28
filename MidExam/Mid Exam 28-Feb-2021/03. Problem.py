def card_add(a_name):
    global cards
    global deck
    if a_name not in cards:
        print(f"Card not found.")
        return deck
    deck.append(a_name)
    return deck


def card_insert(ins_name, ins_index):
    global cards
    global deck
    if 0 <= ins_index < len(deck) and ins_name in cards:
        deck.insert(ins_index, ins_name)
        return deck
    print("Error!")
    return deck


def card_remove(rem_name):
    global cards
    global deck
    if rem_name in deck:
        while rem_name in deck:
            deck.remove(rem_name)
        return deck
    print("Card not found.")
    return deck


def card_swap(c_name1, c_name2):
    global deck
    idx1 = deck.index(c_name1)
    idx2 = deck.index(c_name2)
    deck[idx1], deck[idx2] = deck[idx2], deck[idx1]
    return deck


def card_shuffle():
    global deck
    return deck[::-1]


deck = []
cards = input().split(":")

cmd = input()
while cmd != "Ready":
    cmd = cmd.split()
    if cmd[0] == "Add":
        deck = card_add(cmd[1])
    elif cmd[0] == "Insert":
        deck = card_insert(cmd[1], int(cmd[2]))
    elif cmd[0] == "Remove":
        deck = card_remove(cmd[1])
    elif cmd[0] == "Swap":
        deck = card_swap(cmd[1], cmd[2])
    elif cmd[0] == "Shuffle":
        deck = card_shuffle()

    cmd = input()

print(" ".join([_ for _ in deck]))
