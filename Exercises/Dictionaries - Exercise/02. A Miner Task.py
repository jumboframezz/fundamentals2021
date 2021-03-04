# 2.	A Miner Task
# You will be given a sequence of strings, each on a new line. Every odd line on the console is representing a resource
# (e.g. Gold, Silver, Copper, and so on) and every even – quantity. Your task is to collect the resources and
# print them each on a new line. Print the resources and their quantities in the following format:
# {resource} –> {quantity}
# The quantities will be in the range [1 … 2 000 000 000]

resources = {}
resource_name = input()

while resource_name != "stop":
    resource_qty = int(input())
    if resource_name not in resources:
        resources[resource_name] = resource_qty
    else:
        resources[resource_name] += resource_qty
    resource_name = input()

for _ in resources:
    print(f"{_} -> {resources[_]}")
