def smallest_multiple_n(n):
    counter = n
    number_found = False
    while not number_found:
        for i in range(2, n + 1):
            if counter % i != 0:
                counter += 1
                break
        if i == n:
            number_found = True
    return counter

if __name__ == '__main__':
    print(smallest_multiple_n(3))
