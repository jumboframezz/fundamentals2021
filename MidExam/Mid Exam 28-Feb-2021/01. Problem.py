experience_needed = float(input())
num_battles = int(input())
experience = 0
for battle in range(1, num_battles + 1):
    gained_experience = float(input())
    if battle % 3 == 0:
        experience += gained_experience * 1.15
    elif battle % 5 == 0:
        experience += gained_experience * 0.9
    elif battle % 15 == 0:
        experience += gained_experience * 1.05
    else:
        experience += gained_experience
    if experience >= experience_needed:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        exit(0)
print(f"Player was not able to collect the needed experience, {experience_needed - experience:.2f} more needed.")
