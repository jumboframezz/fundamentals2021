peoples = {}


def p_add(a_arr):
    name, health, energy = a_arr[0], int(a_arr[1]), int(a_arr[2])
    if name in peoples:
        # peoples[name]["energy"] += energy
        peoples[name]["health"] += health
    else:
        peoples[name] = {}
        peoples[name]["energy"] = energy
        peoples[name]["health"] = health
    return peoples


def p_attack(attack_arr):
    attacker, defender, damage = attack_arr[0], attack_arr[1], int(attack_arr[2])
    if attacker not in peoples or defender not in peoples:
        return peoples
    peoples[defender]["health"] -= damage
    if peoples[defender]["health"] <= 0:
        print(f"{defender} was disqualified!")
        del peoples[defender]
    peoples[attacker]["energy"] -= 1
    if peoples[attacker]["energy"] <= 0:
        print(f"{attacker} was disqualified!")
        del peoples[attacker]
    return peoples


def p_delete(d_arr):
    global peoples
    d_name = d_arr[0]
    if d_name == "All":
        del peoples
        peoples = {}
    else:
        if d_name in peoples:
            del peoples[d_name]

    return peoples


line = input()

while line != "Results":
    line = line.split(":")
    cmd = line[0]
    if cmd == "Add":
        peoples = p_add(line[1:])
    elif cmd == "Attack":
        peoples = p_attack(line[1:])
    elif cmd == "Delete":
        peoples = p_delete(line[1:])

    line = input()
а = 5

result = sorted(peoples.items(), key=lambda tkvp: (-tkvp[1]["health"], tkvp[0]))
print(f"People count: {len(peoples)}")


for record in result:
    name = record[0]
    health = record[1]["health"]
    energy = record[1]["energy"]

    print(f"{name} - {health} - {energy}")

