
n = int(input("Enter a number: "))


def ispalindrome(n):
    temp = n
    res = 0
    while temp > 0:
        res = res*10 + temp % 10
        temp //= 10
    return n == res


incre = decre = n

while True:
    if ispalindrome(incre) and ispalindrome(decre) and incre != decre:
        print(incre, decre)
        break
    elif ispalindrome(incre):
        print(incre)
        break
    elif ispalindrome(decre):
        print(decre)
        break
    else:
        incre = incre + 1
        decre = decre - 1
