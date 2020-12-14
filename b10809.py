S = input()
check = [-1] * 26

for i in range(len(S)):
    if check[ord(S[i]) - 97] != -1:
        # ord를 이용한다. a=97 -1이 아니라는건 첫번째로 들어온 수가 있다는 뜻이다.
        continue
    else:
        check[ord(S[i]) - 97] = i
        # ord-97을 해주면 자리가 나오게 된다 if b=98 -> b-a =1 check[1]

for i in range(26):
    print(check[i], end=' ') #end를 통해 띄어쓰기를 하지않고 한칸씩 공백을 두고 프린트한다.