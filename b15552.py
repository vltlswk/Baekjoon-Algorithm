import sys

# 입력값이 매우 많을 때 sys 사용
num = int(input())

for i in range(num):
    x, y = map(int, sys.stdin.readline().split())
    print(x + y)
