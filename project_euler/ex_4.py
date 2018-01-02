def is_palindrome(number):
    product = str(number)
    halfway = len(product) // 2
    for i in range(0, halfway):
        if not product[i] == product[-(i + 1)]:
            return False
    return True

if __name__ == "__main__":
    largest_palindrome = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            prod = x * y
            if is_palindrome(prod):
                if prod > largest_palindrome:
                    largest_palindrome = prod
    print(largest_palindrome)
