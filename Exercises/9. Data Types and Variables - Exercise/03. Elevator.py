# 3.	Elevator
# Calculate how many courses will be needed to elevate n persons by using an elevator with capacity of p persons.
# The input holds two lines: the number of people n and the capacity p of the elevator.

number_of_people = int(input())
elevator_capacity = int(input())

res = number_of_people // elevator_capacity
if number_of_people % elevator_capacity > 0:
    res += 1

print(res)