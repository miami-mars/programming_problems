def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_factors(number):
    fact_list = [1]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            fact_list.append(i)
    prime_list = []
    for x in fact_list:
        if is_prime(x):
            prime_list.append(x)
    return prime_list 
