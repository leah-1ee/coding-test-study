n = int(input())
S = input()

# Please write your code here.
cnt = 0

# C O W 순으로 나오는 모든 조합 세기 
for c in range(n):
    if S[c] == 'C':
        for o in range(c+1, n):
            if S[o] == 'O':
                for w in range(o+1, n):
                    if S[w] == 'W':
                        cnt += 1


print(cnt)