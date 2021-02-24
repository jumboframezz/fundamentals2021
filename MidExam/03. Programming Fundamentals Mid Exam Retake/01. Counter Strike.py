# Problem 1. Counter Strike
# Write a program that keeps track of every won battle against an enemy. You will receive initial energy. Afterwards
# you will start receiving the distance you need to go to reach an enemy until the "End of battle" command is given,
# or until you run out of energy.
# The energy you need for reaching an enemy is equal to the distance you receive. Each time you reach an enemy, your
# energy is reduced. This is considered a successful battle (win). If you don't have enough energy
# to reach an the enemy, print:
#               "Not enough energy! Game ends with {count} won battles and {energy} energy"
#               and end the program.
# Every third won battle increases your energy with the value of your current count of won battles.
# Upon receiving the "End of battle" command, print the count of won battles in the following format:
#               "Won battles: {count}. Energy left: {energy}"
# Input / Constraints
#       •	On the first line you will receive initial energy – an integer [1-10000].
#       •	On the next lines, you will be receiving distance of the enemy – an integer [1-10000]
# Output
#       •	The description contains the proper output messages for each case and the format in which they
#           should be print.


energy = int(input())
distance = input()
won_battles = 0

while distance != "End of battle":
    distance = int(distance)
    if distance > energy:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        exit(0)
    else:
        energy -= distance
        won_battles += 1
        if won_battles % 3 == 0:
            energy += won_battles

    distance = input()

print(f"Won battles: {won_battles}. Energy left: {energy}")
