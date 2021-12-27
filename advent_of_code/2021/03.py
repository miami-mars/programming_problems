def solution(input):
    counter_dict = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0}
    }

    for i in input:
        for pos in range(0, len(i)-1):
            counter_dict[int(pos)][i[int(pos)]] += 1

    gamma_rate = ''
    epsilon_rate = ''

    for k, v in counter_dict.items():
        if v['0'] > v['1']:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    
    print(int(gamma_rate, 2) * int(epsilon_rate,2))


def solution2(input):
    counter_dict = {
        0: {'0': 0, '1': 0},
        1: {'0': 0, '1': 0},
        2: {'0': 0, '1': 0},
        3: {'0': 0, '1': 0},
        4: {'0': 0, '1': 0},
        5: {'0': 0, '1': 0},
        6: {'0': 0, '1': 0},
        7: {'0': 0, '1': 0},
        8: {'0': 0, '1': 0},
        9: {'0': 0, '1': 0},
        10: {'0': 0, '1': 0},
        11: {'0': 0, '1': 0}
    }

    # This is going to require to sort the input and then binary search it
    # against every position.

if __name__ == "__main__":
    with open('03.txt') as f:
        input = f.readlines()

    solution(input)
    solution2(input)