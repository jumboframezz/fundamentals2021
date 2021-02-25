# You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
#   •	If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your
#       initial energy (100). Print: "You gained {0} energy.".
#       After that, print your current energy: "Current energy: {0}.".
#   •	If the event is "order": You've earned some coins, the number in the second part. Each time you get an order,
#       your energy decreases with 30 points.
#       o	If you have energy to complete the order, print: "You earned {0} coins.".
#       o	If your energy drops below 0, you skip the order and gain 50 energy points. Print:
#           "You had to rest!".
#   •	In any other case you are having an ingredient, you have to buy. The second part of the event, contains
#       the coins you have to spent and remove from your coins.
#       o	If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print
#           "You bought {ingredient}."
#       o	If you went bankrupt, print
#           "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the next three lines:
#           "Day completed!", "Coins: {coins}", "Energy: {energy}".
# Input / Constraints
# You will receive a string, representing the working day events, separated with '|' (vertical bar):
#           " event1|event2|event3…".
# Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")
# Output
# Print the corresponding messages, described above.
coins = 100
energy = 100


def rest(r_val):
    global energy
    if energy + r_val <= 100:
        energy += r_val
        print(f"You gained {r_val} energy.")
    else:
        energy_gained = 100 - energy
        energy = 100
        print(f"You gained {energy_gained} energy.")
    print(f"Current energy: {energy}.")


def order(o_val):
    global energy
    global coins
    if energy - 30 >= 0:
        energy -= 30
        coins += o_val
        print(f"You earned {o_val} coins.")
    else:
        print("You had to rest!")
        energy += 50
    return


def buy(item, b_val):
    global coins
    if coins - b_val > 0:
        coins -= b_val
        print(f"You bought {item}.")
        return True
    else:
        print(f"Closed! Cannot afford {item}.")
        return False


line = input().split("|")

for action in line:
    event, val = action.split("-")
    val = int(val)
    if event == "rest":
        rest(val)
    elif event == "order":
        order(val)
    else:
        if not buy(event, val):
            exit(0)

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
