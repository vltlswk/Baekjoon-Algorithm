num = int(input())
arr = []
newarr = []
arr = list(map(int, input().split()))
maxnum = max(arr)

for i in arr:
    newarr.append(i / maxnum * 100)
print(round(sum(newarr) / num, 6))
# round는 소수 n번째 자리까지 보여주는 것 n번째 전에서 반올림한다.
