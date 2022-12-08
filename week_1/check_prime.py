def check_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**1/2) + 1):
            if n % i == 0:
                return False
    return True

while True:
    a = input("Give me a number: ")
    if a.isdigit():
        a = int(a)
    else:
        print("Invalid input")
        break
    print("The number is a prime: ", check_prime(a))