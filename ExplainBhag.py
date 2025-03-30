arr = [1, 2, 4, 8, 8]
firstMax = float('-inf')
for i in arr:
    if i > firstMax:
        firstMax = i
print(firstMax)
secondMax = float('-inf')
for i in arr:
    if firstMax > i > secondMax:
        secondMax = i
print(secondMax)



