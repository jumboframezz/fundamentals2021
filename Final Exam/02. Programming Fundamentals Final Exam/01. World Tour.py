# You are a world traveller and your next goal is to make a world tour. In order to do that, you have to plan out
# everything first. To start with, you would like to plan out all of your stops where you will have a break.
# On the first line you will be given a string containing all of your stops. Until you receive the
# command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
#   •	Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
#   •	Remove Stop:{start_index}:{end_index} – remove the elements of the string from the starting index to
#       the end index (inclusive) if both indices are valid
#   •	Switch:{old_string}:{new_string} – if the old string is in the initial string, replace it with the new
#       one. (all occurrences)
# Note: After each command print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
# Input / Constraints
#   •	JavaScript: you will receive a list of strings
# Output
#   •	Print the proper output messages in the proper cases as described in the problem description
def valid_index(v_index, v_string):
    if 0 <= v_index < len(v_string):
        return True
    return False


def remove_stop(s_index, e_index):
    global travel_string
    if valid_index(s_index, travel_string) and valid_index(e_index, travel_string):
        first_part = travel_string[:s_index]
        second_part = travel_string[e_index + 1:]
        return first_part + second_part
    return travel_string


def add_stop(a_index, a_value):
    if not valid_index(a_index, travel_string):
        return travel_string
    first_part = travel_string[:a_index]
    second_part = travel_string[a_index:]
    return first_part + a_value + second_part


def switch_stop(s_old, s_new):
    global travel_string
    if s_old in travel_string:
        travel_string = travel_string.replace(s_old, s_new)
    return travel_string


travel_string = input()

cmd = input()
while cmd != "Travel":
    cmd, key, value = cmd.split(":")
    if cmd.startswith("Add"):
        travel_string = add_stop(int(key), value)
    elif cmd.startswith("Remove"):
        travel_string = remove_stop(int(key), int(value) )
    elif cmd.startswith("Switch"):
        travel_string = switch_stop(key, value)
    print(travel_string)
    cmd = input()

print(f"Ready for world tour! Planned stops: {travel_string}")