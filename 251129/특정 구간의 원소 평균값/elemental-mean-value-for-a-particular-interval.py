n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0

# i ~ j 범위 지정 
for i in range(n):
    for j in range(i, n):
        # 범위 안에서 탐색 
        for k in range(i, j+1):
            # 평균값 구하기 
            avg = sum(arr[i:j+1])/len(arr[i:j+1])
            # 원소=평균값 이면 
            if arr[k] == avg:
                # cnt + 1, 다음 구간으로 
                cnt += 1
                break

print(cnt)