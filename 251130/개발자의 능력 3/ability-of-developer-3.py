abilities = list(map(int, input().split()))

# Please write your code here.
# 개발자 수, 능력 총 합, 차이 최솟값 저장 
n = len(abilities)
total = sum(abilities)
min_diff = float('inf')

# 개발자 3명 조합 
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            # g1, g2 능력 합 계산 
            group1 = abilities[i] + abilities[j] + abilities[k]
            group2 = total - group1
            # 차이 계산, 최솟값 업데이트 
            diff = abs(group1 - group2)
            min_diff = min(min_diff, diff)


print(min_diff)