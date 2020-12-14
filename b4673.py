# 1 -> 2 -> 4 -> 8 -> 16 -> 23 -> 28 -> 38 -> 49 -> 62
# 3 -> 6 -> 12 -> 15 -> 21 -> 24 -> 30 ->
# 5 -> 10 -> 11 -> 13 ->
# 7 -> 14 -> 19 -> 29 -> 40 ->
# 9 -> 18 -> 27 -> 36 -> 45 -> 54 -> 63 -> 72 -> 81 -> 90 -> 99 -> 117 -> ...
arr = []

def addNoneSelfNum(num):
    n = 0
    while num <= 10000:
        for i in range(len(str(num))):
            n += int(str(num)[i])
        num += n
        n = 0
        if num <= 10000:
            arr.append(num)
    print(arr)


addNoneSelfNum(1)
