import re

pat_name = r"(?P<name>[^\+\-\*/0-9\.]+)"

line = input().split(", ")
for daemon in line:
    daemon_name = re.findall(pat_name, daemon)
    daemon_name = "".join(daemon_name)
    print(daemon_name)
