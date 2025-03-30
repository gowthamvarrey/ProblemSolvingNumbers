num = int(input())
flag = 0
square = num ** 2
mul = 10

while square % mul <= num:
    if square % mul == num:
        flag = 1
        break
    mul *= 10
print("Yes, its a automorphic number...") if flag else print("Not a automorphic number")
