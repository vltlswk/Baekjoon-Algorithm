hour, minute = map(int, input().split())
# 1번 24시(=0시)면서 45분 미만
# 2번 45분 미만
# 3번 45분 이상

dif: int = 0
if hour == 0 and minute < 45:
    hour = 23
    dif = 45 - minute
    minute = 60 - dif
    print(hour, minute)
elif minute < 45:
    hour = hour - 1
    dif = 45 - minute
    minute = 60 - dif
    print(hour, minute)
else:
    minute = minute - 45
    print(hour, minute)
