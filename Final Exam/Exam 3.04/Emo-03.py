command = input().split(":")
players = {}
while not command[0] == "Results":
    if command[0] == "Add":
        player, health, energy = command[1], int(command[2]), int(command[3])
        if player not in players:
            players[player] = {'health': health, 'energy': energy}
        else:
            players[player]['health'] += health
    elif command[0] == "Attack":
        attacker, defender, damage = command[1], command[2], int(command[3])
        if attacker in players and defender in players:
            players[defender]['health'] -= damage
            players[attacker]['energy'] -= 1
            if players[defender]['health'] <= 0:
                players.pop(defender)
                print(f"{defender} was disqualified!")
            if players[attacker]['energy'] <= 0:
                players.pop(attacker)
                print(f"{attacker} was disqualified!")
    elif command[0] == "Delete":
        player = command[1]
        if not player == "All":
            players.pop(player)
        else:
            players.clear()
    command = input().split(":")


sorted_players = dict(sorted(players.items(), key=lambda x: (-x[1]['health'], x[0])))
print(f"People count: {len(sorted_players)}")
for player in sorted_players:
    print(f"{player} - {sorted_players[player]['health']} - {sorted_players[player]['energy']}")