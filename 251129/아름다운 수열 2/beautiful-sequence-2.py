N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# 아름다운 수열을 세는 변수 
cnt = 0

# A 배열을 순회하며 아름다운 수열을 찾음 
for i in range(len(A)-len(B)+1):
    # 정렬했을 때 같으면 아름다운 수열 
    if sorted(A[i:i+len(B)]) == sorted(B):
        cnt += 1


print(cnt)