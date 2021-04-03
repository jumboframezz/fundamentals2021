import re

#  cmd_patt = r"((?<=\!))(?P<cmd>[A-Z][a-z]{2,})(\!:)"
cmd_patt = r"((?<=\!))(?P<cmd>[A-Z][a-z]{2,})(\!:)\[(?P<msg>[A-Za-z]{8,})\]"

n = int(input())
for i in range(n):
    line = input()
    command = [d.groupdict() for d in re.finditer(cmd_patt, line)]

    if len(command) > 0:
        cmd = command[0]['cmd']
        msg = command[0]['msg']
        rez = " ".join([str(ord(_)) for _ in msg])
        print(f"{cmd}: {rez}")

    else:
        print("The message is invalid")

