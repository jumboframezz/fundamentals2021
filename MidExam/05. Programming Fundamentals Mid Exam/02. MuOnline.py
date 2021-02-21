# You have initial health 100 and initial bitcoins 0. You will be given a string, representing the dungeons rooms.
# Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
#   • "potion"
#       o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
#       o	First print: "You healed for {amount} hp.".
#       o	After that, print your current health: "Current health: {health} hp.".
# •	"chest"
#       o	You've found some bitcoins, the number in the second part.
#       o	Print: "You found {amount} bitcoins."
# •	In any other case you are facing a monster, you are going to fight. The second part of the room, contains the
# attack of the monster. You should remove the monster's attack from your health.
#       o	If you are not dead (health <= 0) you've slain the monster, and you should print ("You slayed {monster}.")
#       o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room
#           you`ve manage to reach:
#               "Best room: {room}".
# If you managed to go through all the rooms in the dungeon, print on the next three lines:
#               "You've made it!", "Bitcoins: {bitcoins}", "Health: {health}".
# Input / Constraints
# You receive a string, representing the dungeons rooms, separated with '|' (vertical bar): "room1|room2|room3…".


health = 100
bitcoins = 0
room_no = 1

line = input().split("|")

for room in line:
    command, value = room.split()
    value = int(value)
    if command == "potion":
        if health + value > 100:
            healed = 100 - health
            health = 100
        else:
            healed = value
            health += value
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {value} bitcoins.")
        bitcoins += value
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_no}")
            exit(0)
    room_no += 1
print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
