# You are a mathematician during world war 2, who has joined the cryptography team to decipher the enemy's enigma code.
# Your job is to create a program to crack the codes.
# On the first line of the input you will receive the encrypted message. After that, until the "Decode" command is
# given, you will be receiving strings with instructions for different operations that need to be performed upon the
# concealed message to interpret it and reveal its true content. There are several types of instructions, split by '|'
#   Move {number of letters}
#       Moves the first n letters to the back of the string.
#   Insert {index} {value}
#       Inserts the given value before the given index in the string.
#   ChangeAll {substring} {replacement}
#       Changes all occurrences of the given substring with the replacement text.
#   Input / Constraints
#       On the first line, you will receive a string with message.
#       On the next lines, you will be receiving commands, split by '|' .
#   Output
#       After the "Decode" command is received, print this message:
#       "The decrypted message is: {message}"


def move(num_letters):
    first_slice = encrypted_message[:num_letters]
    second_slice = encrypted_message[num_letters:]
    return second_slice + first_slice


def s_insert(idx, value):
    s_list = [_ for _ in encrypted_message]
    s_list.insert(idx, value)
    return "".join(s_list)


def change_all(needle, haystack):
    return encrypted_message.replace(needle, haystack)


encrypted_message = input()
command = input()
while command != "Decode":
    arr = command.split("|")
    cmd, arg = arr[0], arr[1]
    if cmd == "Move":
        encrypted_message = move(int(arg))
    elif cmd == "Insert":
        val = arr[2]
        encrypted_message = s_insert(int(arg), val)
    elif cmd == "ChangeAll":
        val = arr[2]
        encrypted_message = change_all(arg, val)
    command = input()


print(f"The decrypted message is: {encrypted_message}")
