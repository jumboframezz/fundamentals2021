# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the
# gifts you plan on buying on a single line, separated by space, in the following format:
#       "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#   •	"OutOfStock {gift}"
#       o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
#   •	"Required {gift} {index}"
#       o	Replace the value of the current gift on the given index with this gift, if the index is valid.
#   •	"JustInCase {gift}"
#       o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in
# the following format:
#       "{gift1} {gift2} {gift3}… {giftn}"
# Input / Constraints
#   •	On the 1st line you are going to receive the names of the gifts, separated by a single space.
#   •	On the next lines, until the "No Money" command is received, you will be receiving commands.
#   •	The input will always be valid.
# Output
#   •	Print the gifts in the format described above.
def out_of_stock(os_gift):
    while os_gift in line:
        idx = line.index(os_gift)
        line[idx] = "None"
    return line


def required(rq_gift, rq_index):
    if 0 <= rq_index < len(line):
        line[rq_index] = rq_gift
    return line


def just_in_case(jc_gift):
    line[-1] = jc_gift
    return line


line = input().split()
command = input()
while command != "No Money":
    params = command.split()
    cmd = params[0]
    if cmd == "OutOfStock":
        line = out_of_stock(params[1])
    elif cmd == "Required":
        gift = params[1]
        idx = int(params[2])
        line = required(gift, idx)
    elif cmd == "JustInCase":
        line = just_in_case(params[1])

    command = input()

print(" ".join([_ for _ in line if _ != "None"]))

