num = int(input())
arr = []
score = 0
total = [0 for i in range(num)]
for i in range(num):
    arr.append(input())

for i in range(len((arr))):
    score = 0
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            score += 1
            total[i] += score
        elif arr[i][j] == 'X':
            score = 0

for i in range(num):
    print(total[i])