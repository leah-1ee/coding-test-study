N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
# 범위 set으로 만들기 
a1, b1, c1 = a1+N, b1+N, c1+N
a2, b2, c2 = a2+N, b2+N, c2+N
a1_scope = set(i%N for i in range(a1-2, a1+3))
a2_scope = set(i%N for i in range(a2-2, a2+3))
b1_scope = set(i%N for i in range(b1-2, b1+3))
b2_scope = set(i%N for i in range(b2-2, b2+3))
c1_scope = set(i%N for i in range(c1-2, c1+3))
c2_scope = set(i%N for i in range(c2-2, c2+3))


# 조합 수 저장
cnt = 0

# 모든 조합 탐색 
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            ii, jj, kk = i % N, j % N, k % N
            # 조합 1, 2에 대하여 각각 열리는지 확인 
            key1 = (ii in a1_scope) and (jj in b1_scope) and (kk in c1_scope)
            key2 = (ii in a2_scope) and (jj in b2_scope) and (kk in c2_scope)
            # 두 조합 중 하나라도 만족하면 cnt + 1
            if key1 or key2:
                cnt += 1

print(cnt)
