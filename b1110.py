num = input()  # 숫자 받기 10보다 작으면 0붙여 2자리수
originNum = num
newnum = 0
count = 0

while True:
    if int(num) < 10 and len(num)<2:
        num = "0" + num
    newnum = int(num[0]) + int(num[1])
    if newnum < 10:
        num = str(num[1]) + str(newnum)[0]
        count += 1
    else:
        num = str(num[1]) + str(newnum)[1]
        count += 1

    if int(num) == int(originNum):
        print(count)
        break
