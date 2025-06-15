n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

while True:
    # 최댓값 인덱스 출력 
    i = a.index(max(a))
    print(i+1, end=' ')

    # 최댓값 왼쪽만 남기기 
    a = a[0:i]

    # 배열이 비면 종료 
    if i<=0:
        break
