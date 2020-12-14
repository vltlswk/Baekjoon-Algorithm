num= int(input())
overnum = 99
if num >= 100:
    if len(str(num)) == 3:
         for i in range(100, num + 1):
            if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
                overnum += 1
            else:
                pass
         print(overnum)
    elif len(str(num)) == 4:
        print("144")

else:
    print(num)
