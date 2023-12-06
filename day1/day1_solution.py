import re


values = []
with open("day1_input.txt") as file:
    for line in file:
        values.append(line.rstrip())

result = 0
for line in values:
    digits_only = re.sub(r'\D', '', line)
    result += int(digits_only[0] + digits_only[-1])
print(result)
