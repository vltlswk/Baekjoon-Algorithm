import sys

count, cut = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    if cut > i: print(i)
