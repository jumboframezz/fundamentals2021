# You have now returned from your world tour. On your way you have discovered some new plants and you want to
# gather some information about them and create an exhibition to see which plant is highest rated.
# On the first line you will receive a number n. On the next n lines, you will be given some information
# about the plants that you have discovered in the format:
#               "{plant}<->{rarity}".
# Store that information, because you will need it later. If you receive a plant more than once, update its rarity.
# After that until you receive the command "Exhibition" you will be given some of these commands:
#   •	Rate: {plant} - {rating} – add the given rating to the plant (store all ratings)
#   •	Update: {plant} - {new_rarity} – update the rarity of the plant with the new one
#   •	Reset: {plant} – remove all the ratings of the given plant
# Note: If any of the command is invalid, print "error"
# After the command "Exhibition" print the information that you have about the plants in the following format:
# Plants for the exhibition:
#   - {plant_name}; Rarity: {rarity}; Rating: {average_rating formatted to the 2nd digit}
# …
# The plants should be sorted by rarity descending, then by average rating descending
# Input / Constraints
# •	You will recive the input as described above
# •	JavaScript: you will receive a list of strings
# Output
# •	Print the information about all plants as described above

def rate(r_args):
    rate_plant, r_rating = r_args.split(" - ")
    if rate_plant not in plants:
        print("error")
        return plants
    plants[rate_plant]["rating"].append(int(r_rating))
    return plants


def update(u_arr):
    u_plant, new_rarity = u_arr.split(" - ")
    if u_plant not in plants:
        print("error")
        return plants
    plants[u_plant]["rarity"] = int(new_rarity)
    return plants


def rst(rst_arr):
    r_plant = rst_arr
    if r_plant not in plants:
        print("error")
        return plants
    plants[r_plant]["rating"].clear()
    return plants


plants = {}
n = int(input())
for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {"rarity": int(rarity), "rating": []}


cmd = input()
while cmd != "Exhibition":
    cmd, args = cmd.split(": ")
    if cmd == "Rate":
        plants = rate(args)
    elif cmd == "Update":
        plants = update(args)
    elif cmd == "Reset":
        plants = rst(args)
    else:
        print("error")
    cmd = input()

# Calculate and add average rating for every plant in dict
for plant_name, value in plants.items():
    if value['rating']:
        avg = sum(value['rating']) / len(value['rating'])
    else:
        avg = 0
    plants[plant_name]['avg'] = avg

result = sorted(plants.items(), key=lambda tkvp: (-tkvp[1]['rarity'], -tkvp[1]['avg']))
print("Plants for the exhibition:")
for plant_name, values in result:
    print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: {values['avg']:.2f}")

