from math import sqrt

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_factors(fact_list):
    prime_list = []
    for x in fact_list:
        if is_prime(x):
            prime_list.append(x)
    return prime_list 

def factors(number):
    fact_list = [1]
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            fact_list.append(i)
    fact_list.append(number)
    return fact_list

if __name__ == '__main__':
    factor_list = factors(600851475143)
    prime_list = prime_factors(factor_list)
    print(prime_list)
