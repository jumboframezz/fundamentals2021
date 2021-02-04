# 10.	* Gladiator Expenses
# As a gladiator, Peter has to repair his broken equipment when he loses a fight. His equipment consists of helmet,
# sword, shield and armor. You will receive the Peter`s lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also brakes.
# Every second time, when his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment. Calculate his expenses for the year
# for renewing his equipment.
# Input / Constraints
# The input will consist of 5 lines:
#   •	On the first line you will receive the lost fights count – integer in the range [0, 1000].
#   •	On the second line you will receive the helmet price - floating point number in range [0, 1000].
#   •	On the third line you will receive the sword price - floating point number in range [0, 1000].
#   •	On the fourth line you will receive the shield price - floating point number in range [0, 1000].
#   •	On the fifth line you will receive the armor price - floating point number in range [0, 1000].
# Output
#   •	As output you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"

lost_count = int(input())
broken_helmet = False
broken_sword = False
broken_shield = False
broken_armor =False

for battle in range(1, lost_count + 1):

    broken_helmet = True if battle % 2 == 0 else False
    broken_sword = True if battle % 3 == 0 else False
    if broken_sword and broken_helmet:
        pass
