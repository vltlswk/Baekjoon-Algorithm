num = int(input())

total = 0
avg = 0

for i in range(num):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]
    # 평균값을 첫 번째(인원수)로 나누기
    count = 0
    for j in arr[1:]:
        # 여기서 주의할점은 arr이 1부터 시작해야 한다.
        if j > avg:
            count += 1
    rate = count / arr[0] * 100
    print(format(rate, ".3f") + "%")
    # 프린트 형식에 format을 넣어서 소수점 3자리까지 출력
