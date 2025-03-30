n = int(input("Enter a number: "))

def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

incre ,decre = n+1, n-1

if isprime(n):
    print(n)
else:
    while True:
        if isprime(incre) and isprime(decre):
            print(incre, decre)
            break
        elif isprime(incre):
            print(incre)
            break
        elif isprime(decre):
            print(decre)
            break
        else:
            incre = incre + 1
            decre = decre - 1
