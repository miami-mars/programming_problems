def part1(input):
    horizontal_position = 0
    depth = 0

    for line in input:
        command, value = line.split(' ')
        if command == 'forward':
            horizontal_position += int(value)
        elif command == 'down':
            depth += int(value)
        else:
            depth -= int(value)

    print(horizontal_position)
    print(depth)
    print(horizontal_position * depth)

def part2(input):
    horizontal_position = 0
    depth = 0
    aim = 0

    for line in input:
        command, value = line.split(' ')
        if command == 'forward':
            horizontal_position += int(value)
            depth += int(value) * aim
        elif command == 'down':
            aim += int(value)
        else:
            aim -= int(value)

    print(horizontal_position)
    print(depth)
    print(horizontal_position * depth)


if __name__ == "__main__":
    with open('02.txt') as f:
        input = f.readlines()
    part1(input)
    part2(input)