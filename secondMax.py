arr = [1, 2, 4, 8, 8]
firstMax = float('-inf')
secondMax = float('-inf')
for i in arr:
    if i > firstMax:
        secondMax = firstMax
        firstMax = i
    elif i > secondMax and i != firstMax:
        secondMax = i
print(firstMax,secondMax)





