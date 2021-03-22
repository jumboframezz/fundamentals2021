def add(a_arr):
    a_piece, a_composer, a_key = a_arr[1:]
    for _ in pieces:
        if _["name"] == a_piece:
            print(f"{a_piece} is already in the collection!")
            return pieces
    pieces.append({"name": a_piece, "composer": a_composer, "key": a_key})
    print(f"{a_piece} by {a_composer} in {a_key} added to the collection!")
    return pieces


def remove_piece(r_arr):
    r_piece = r_arr[1]
    for idx in range(len(pieces)):
        if pieces[idx]['name'] == r_piece:
            pieces.pop(idx)
            print(f"Successfully removed {r_piece}!")
            return pieces
    print(f"Invalid operation! {r_piece} does not exist in the collection.")
    return pieces


def change_key(c_arr):
    c_name, c_key = c_arr[1:]
    for idx in range(len(pieces)):
        if pieces[idx]['name'] == c_name:
            pieces[idx]['key'] = c_key
            print(f"Changed the key of {c_name} to {c_key}!")
            return pieces
    print(f"Invalid operation! {c_name} does not exist in the collection.")
    return pieces


num_pieces = int(input())
pieces = []
for _ in range(num_pieces):
    piece, composer, key = input().split("|")
    pieces.append({"name": piece, "composer": composer, "key": key})

command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        pieces = add(command)
    elif command[0] == "Remove":
        pieces = remove_piece(command)
    elif command[0] == "ChangeKey":
        pieces = change_key(command)

    command = input()

for piece in sorted(pieces, key=lambda x: (x["name"], x["composer"])):
    print(f"{piece['name']} -> Composer: {piece['composer']}, Key: {piece['key']}")
