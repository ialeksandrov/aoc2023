with open("day2_input.txt", 'r') as file:
    lines = file.read()


def part1_solution(lines):

    possible = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = 0
    for id, game in enumerate(lines.split('\n'), start=1):
        game = game.split(': ')[1]
        for hand in game.split('; '):
            is_possible = False
            for subset in hand.split(', '):
                n, color = subset.split()
                if int(n) > possible[color]:
                    is_possible = True
                    break
            if is_possible:
                break
        else:
            possible_games += id

    return possible_games


def part2_solution(lines):
    power = 0
    for game in lines.split('\n'):
        game = game.split(': ')[1]
        max_number = {'red': 0, 'green': 0, 'blue': 0}
        for hand in game.split('; '):
            for subset in hand.split(', '):
                n, color = subset.split()
                max_number[color] = max(int(n), max_number[color])

        power += max_number['red'] * max_number['green'] * max_number['blue']
    return power

print('Part 1:', part1_solution(lines))
print('Part 2:', part2_solution(lines))