# On the first line of the input you will receive the concealed message. After that, until the
# "Reveal" command is given, you will be receiving strings with instructions for different operations that
# need to be performed upon the concealed message in order to interpret it and reveal its true content. There are
# several types of instructions, split by ":|:"
#   •	InsertSpace:|:{index}
#       o	Inserts a single empty space at the given index. The given index will always be valid.
#   •	Reverse:|:{substring}
#       o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#       o	If not, print "error".
#       o	This operation should replace only the first occurrence of the given substring if
#           there are more than one such occurrences.
#   •	ChangeAll:|:{substring}:|:{replacement}
#       o	Changes all occurrences of the given substring with the replacement text.
#    Input / Constraints
#   •	On the first line, you will receive a string with message.
#   •	On the next lines, you will be receiving commands, split by ":|:".
# Output
#   •	After each set of instructions, print the resulting string.
#   •	After the "Reveal" command is received, print this message:
# "You have a new text message: {message}"


def insert_space(i_arr):
    global message
    idx = int(i_arr[0])
    first_part = message[:idx]
    second_part = message[idx:]
    return first_part + " " + second_part


def reverse_subs(r_arr):
    global message
    substring = r_arr[0]
    if substring not in message:
        return message
    reversed_sub = substring[::-1]
    return message.replace(substring, "", 1) + reversed_sub


def change_all(c_arr):
    global message
    old_string = c_arr[0]
    new_string = c_arr[1]
    return message.replace(old_string, new_string)


message = input()

cmd = input()
while not cmd == "Reveal":
    cmd = cmd.split(":|:")
    if cmd[0] == "InsertSpace":
        message = insert_space(cmd[1:])
    elif cmd[0] == "Reverse":
        if cmd[1] not in message:
            print("error")
            cmd = input()
            continue
        message = reverse_subs(cmd[1:])
    elif cmd[0] == "ChangeAll":
        message = change_all(cmd[1:])

    print(message)
    cmd = input()

print(f"You have a new text message: {message}")
