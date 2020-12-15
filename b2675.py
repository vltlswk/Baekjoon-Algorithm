import sys

num = int(input())
arr = []
for i in range(num):
    arr.append(sys.stdin.readline().split())
for i in range(len((arr))):
    for j in range(len(arr[i][1])):
        print(arr[i][1][j] * int(arr[i][0]), end="")
    print()
