with open('day9_input.txt', 'r') as file:
    lines = file.read()


def part1_solution(lines):
    total = 0
    for line in lines.split('\n'):
        nums = [int(n) for n in line.split()]
        final_nums = []

        while set(nums) != {0}:
            final_nums.append(nums[-1])
            nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        total += sum(final_nums)

    return total


def part2_solution(lines):
    total = 0
    for line in lines.split('\n'):
        nums = [int(n) for n in line.split()]
        first_nums = []

        while set(nums) != {0}:
            first_nums.append(nums[0])
            nums = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        for i, num in enumerate(first_nums):
            total += num if i % 2 == 0 else -num

    return total


print('Part 1:', part1_solution(lines))
print('Part 2:', part2_solution(lines))
