countArr = [0 for i in range(10)]
A = int(input())
B = int(input())
C = int(input())

total = A * B * C

for i in range(len(str(total))):
    for j in range(10):
        if str(j) == str(total)[i]:
            countArr[j] += 1

for i in countArr:
    print(i)