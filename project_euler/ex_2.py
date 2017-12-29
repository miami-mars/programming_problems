def evn_fib_sum():
    sum = 0
    fib_1 = 1
    fib_2 = 2
    while fib_2 < 4000000:
        if fib_2 % 2 == 0:
            sum += fib_2
        fib_next = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_next
    return sum
