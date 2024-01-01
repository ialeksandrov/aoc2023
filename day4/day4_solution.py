import re


with open('day4_input.txt', 'r') as file:
    lines = file.read()


def part1_solution(lines):
    regex = r':(.*?)\|(.*)'
    points = 0
    for line in lines.split('\n'):
        nums = re.search(regex, line)
        win_num = set(map(int, nums.group(1).split()))
        true_num = set(map(int, nums.group(2).split()))
        n_matches = len(win_num & true_num)
        if n_matches:
            points += 2 ** (n_matches - 1)

    return points


def part2_solution(lines):
    lines = lines.split('\n')
    cards = [1] * len(lines)
    regex = r':(.*?)\|(.*)'
    for item, line in enumerate(lines):
        nums = re.search(regex, line)
        win_num = set(map(int, nums.group(1).split()))
        true_num = set(map(int, nums.group(2).split()))
        n_matches = len(win_num & true_num)
        for j in range(item + 1, item + 1 + n_matches):
            cards[j] += cards[item]

    return sum(cards)


print('Part 1:', part1_solution(lines))
print('Part 2:', part2_solution(lines))