import re
from operator import mul

with open('day3_input.txt', 'r') as f:
    lines = f.read()


def part1_solution(lines):

    lines = lines.split('\n')

    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for i, line in enumerate(lines):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                part_num_sum += int(m.group())

    return part_num_sum


def part2_solution(lines):
    lines = lines.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum



print('Part 1:', part1_solution(lines))
print('Part 2:', part2_solution(lines))
