n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
# 최소 거리 저장 
min_dist = float('inf')

# i번 방에서 시작한다고 가정
for i in range(n):
    # 거리 저장 
    dist = 0
    
    # 거리 합 계산 
    for j in range(n):

        dist += ((i + j + 1) % n) * a[j]

    # 최솟값 업데이트 
    min_dist = min(min_dist, dist)


print(min_dist)


'''
거리
n = 5
i = 0
j = 0 - 0, 1 - 1, 2 - 2, 3 - 3, 4 - 4
i = 1
j = 0 - 4, 1 - 0, 2 - 1, 3 - 2, 4 - 3
i = 2
j = 0 - 3, 1 = 4, 2 = 0, 3 = 1, 4 = 2

i + j + 1 mod n
'''