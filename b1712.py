a, b, c = map(int, input().split())
i = 0

if b >= c:
    print("-1")
else:
    i = a // (c - b)
    print(i + 1)

# a, b, c = map(int, input().split())
# diff = 0
# # a는 고정금액
# # b는 가변금액
# # c는 노트북 가격
# # c*n>a+nb
# # 손익 분기점이 없다=-1
#
# if b >= c:
#     print("-1")
# else:
#     diff = c - b
#     i = 2
#     while True:
#         if diff * i > a:
#             print(i)
#             break
#         else:
#             i += 1