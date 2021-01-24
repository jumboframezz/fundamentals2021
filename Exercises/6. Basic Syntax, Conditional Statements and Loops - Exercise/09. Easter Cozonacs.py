#
# * Easter Cozonacs
# Since it’s Easter you have decided to make some cozonacs and exchange them for eggs.
# Create a program that calculates how much cozonacs you can make with the budget you have. First, you
# will receive your budget. Then, you will receive the price for 1 kg flour. Here is the recipe for one
# cozonac:
# Eggs      1 pack
# Flour     1 kg
# Milk      0.250 l
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than
# price for 1 kg flour. Notice, that you need 0.250l milk for one cozonac and the calculated price is for 1l.
# Start cooking the cozonacs and keep making them until you have enough budget. Keep in mind that:
# For every cozonac that you make, you will receive 3 colored eggs.
# For every 3rd cozonac that you make, you will lose some of your colored eggs after you have received the
# usual 3 colored eggs for your cozonac. The count of eggs you will lose is calculated when you subtract
# 2 from your current count of cozonacs – ({currentCozonacsCount} – 2)
# In the end, print the cozonacs you made, the eggs you have gathered and the money you have left, formatted to
# the 2nd decimal place, in the following format:
# ￼"You made {countOfCozonacs} cozonacs! Now you have {coloredEggs} eggs and {moneyLeft}BGN left."
# Input / Constraints
# On the 1st line you will receive the budget – a real number in the range [0.0…100000.0]
# On the 2nd line you will receive the price for 1 kg flour – a real number in the range [0.0…100000.0]
# The input will always be in the right format.
# You will always have a remaining budget.
# There will not be a case in which the eggs become a negative count.
# Output
# In the end print the count of cozonacs you have made, the colored eggs you have gathered and the money
# formatted to the 2nd decimal place in the format described above.

budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price_per_l = flour_price * 1.25
milk_price = milk_price_per_l / 4
colored_eggs = 0
coz_count = 0
coz_price = flour_price + milk_price + egg_price

while budget >= coz_price:
    budget -= coz_price
    colored_eggs += 3
    coz_count += 1
    if coz_count % 3 == 0:
        colored_eggs -= (coz_count - 2)

print(f"You made {coz_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
