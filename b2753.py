# 윤년이면 1 윤년이 아니면 0
# 윤년 %4==0 and 윤년 %100!=100 or 윤년%400==0

year=int(input())

if year % 4 != 0:
    #4의 배수가 아닐때
    print("0")

elif year%100!=0 and year % 4 == 0:
    #100의 배수아니고 4의 배수 일때
    print("1")

elif year%100==0 and year %400!=0:
    #100의 배수고 400의 배수가 아닐때
    print("0")

elif year%400==0:
    print("1")


