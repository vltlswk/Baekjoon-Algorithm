arr = []
for i in range(10):
    arr.append(int(input()))
remainder = 0
total = 0
arrR = [0 for i in range(42)]
for i in arr:
    remainder = i % 42
    arrR[remainder] += 1

for i in arrR:
    if i >= 1:
        total += 1
print(total)
