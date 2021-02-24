# Most football fans love it for the goals and excitement. Well, this problem doesn't. You are to handle the referee's
# little notebook and count the players who were sent off for fouls and misbehavior.
# The rules: Two teams, named "A" and "B" have 11 players each. The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card. If one of the teams has less than 7 players
# remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.
#
# A card is a string with the team's letter ('A' or 'B') followed by a single dash and player's number. e.g. the
# card 'B-7' means player #7 from team B received a card.
# The task: Given a list of cards (could be empty), return the number of remaining players on each team at the
# end of the game in the format:
#   "Team A - {players_count}; Team B - {players_count}".
#   If the game was terminated print an additional line: "Game was terminated"
# Note for the random tests: If a player that has already been sent off receives another card - ignore it.
# Input
# The input (the cards) will come on a single line separated by a single space.
# Output
# Print the remaining players as described above and add another line (as shown above) if the game was terminated.

line = input().split()
a_team = [_ for _ in range(1, 12)]
b_team = [_ for _ in range(1, 12)]
a_team_len = 11
b_team_len = 11
for card in line:
    team, player = card.split("-")
    player = int(player)
    if team == "A" and player in a_team:
        a_team.remove(player)
    elif team == "B" and player in b_team:
        b_team.remove(player)
    a_team_len = len(a_team)
    b_team_len = len(b_team)
    if a_team_len < 7 or b_team_len < 7:
        break
print(f"Team A - {a_team_len}; Team B - {b_team_len}")

if a_team_len < 7 or b_team_len < 7:
    print("Game was terminated")
