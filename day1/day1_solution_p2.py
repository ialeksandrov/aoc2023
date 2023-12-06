import re


values = []
with open("day1_input.txt") as file:
    for line in file:
        values.append(line.rstrip())
result = 0
replacements_dictionary = {'one': 'on1e', 'two': 'tw2o', 'three': 'thr3e', 'four': 'fo4ur', 'five': 'fi5ve',
                           'six': 'si6x', 'seven': 'sev7en', 'eight': 'ei8ght', 'nine': 'ni9ne'}

for line in values:
    for key, value in replacements_dictionary.items():
        line = line.replace(key, value)
    print(line)
    digits_only = re.sub(r'\D', '', line)
    result += int(digits_only[0] + digits_only[-1])

print(result)
