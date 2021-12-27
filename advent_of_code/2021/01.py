def part1(input):
    counter = 0
    last = 0
    for i in input:
        if last == 0:
            next
        else:
            if int(i) > last:
                counter += 1
        last = int(i)

def part2(input):
    sums = []
    for i in range(0, len(input) - 2):
        sums.append(int(input[i]) + int(input[i+1]) + int(input[i+2]))
    part1(sums)

if __name__ == "__main__":
    with open('01.txt') as f:
        input = f.readlines()
    part1(input)
    part2(input)