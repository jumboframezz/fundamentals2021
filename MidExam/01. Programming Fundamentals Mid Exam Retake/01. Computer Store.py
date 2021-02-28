# Write a program that prints you a receipt for your new computer. You will receive the prices (without tax) of the
# parts until you receive what type of customer is this - special or regular. Once you receive the type of the
# customer you should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, then he has a 10% discount of the price of the total price with taxes.
# If a given price is not positive number, you should print "Invalid price!" on the console and continue with
# the next price.
# If total price is equal to zero, you should print "Invalid order!" on the console.
# Input
#   •	You will receive numbers representing prices (without tax) until command "special" or "regular":
# Output
#   •	The receipt should be in the following format:
#
#       "Congratulations you've just bought a new computer!
#        Price without taxes: {total price without taxes}$
#        Taxes: {total amount of taxes}$
#        -----------
#        Total price: {total price with taxes}$"
# Constraints
# Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only on
# the total price.  Discount is only applicable to the final price!

line = input()
subtotal = 0.0
while not (line == "special" or line == "regular"):
    part_price = float(line)
    if part_price > 0:
        subtotal += float(line)
    else:
        print("Invalid price!")
    line = input()
total = subtotal * 1.2
if line == "special":
    total = total * 0.9
if total <= 0:
    print("Invalid order!")
    exit(0)
print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {subtotal:.2f}$")
print(f"Taxes: {subtotal * 0.2:.2f}$")
print("-----------")
print(f"Total price: {total:.2f}$")
