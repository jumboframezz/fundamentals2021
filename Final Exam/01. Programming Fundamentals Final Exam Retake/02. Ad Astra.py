#  (?P<food>(#|\|)[A-Z][a-z]+)(\2)\d{2}\/\d{2}\/\d{2}\2
#  (?P<food>(#|\|)([A-Z][a-z]+))(\2)(?P<date>\d{2}\/\d{2}\/\d{2})\2(?P<energy>\d+)\2
#  ((?<=#|\|)([A-Z][a-z]+))
#  (?P<separator>#|\|)(?P<food>([A-Z][a-z]+))(?P=separator)(?P<date>\d{2}\/\d{2})\/\d{2}(?P=separator)(?P<energy>\d+)(?P=separator)
# (?P<sep>#|\|)(?P<food>([A-Z][a-z]+)(\s[A-Z][a-z]+)?)+(?P=sep)(?P<date>\d{2}\/\d{2}\/\d{2})(?P=sep)(?P<energy>\d+)(?P=sep)
import re

pat = r"(?P<sep>#|\|)(?P<food>([A-Z][a-z]+\s?)+)(?P=sep)(?P<date>\d{2}\/\d{2}\/\d{2})(?P=sep)(?P<energy>\d+)(?P=sep)"


line = input()
# line = "$$#@@%^&#Fish#24/12/20#8500#|#Incorrect#19.03.20#450|$5*(@!#Ice Cream#03/10/21#9000#^#@aswe|Milk|05/09/20|2000|"
total_energy = 0
valid_data = [match_obj.groupdict() for match_obj in re.finditer(pat, line)]
for food in valid_data:
    total_energy += int(food["energy"])
print(f"You have food to last you for: {int(total_energy / 2000) } days!")


for food in valid_data:
    print(f"Item: {food['food']}, Best before: {food['date']}, Nutrition: {food['energy']}")

