n, k = map(int, input().split()) # n 명, k 크기 
x = [] # 위치
c = [] # 알파벳 
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
# 위치에 따른 알파벳 기록할 배열 
max_val = max(max(x)+1, k+1)
arr = [0] * max_val

# 알파벳 기록 
for i in range(len(x)):
    arr[x[i]] = c[i]


max_cnt = 0
# 최대 점수 구하기 
for i in range(len(arr)-k):
    cnt = 0
    for j in range(i, i+k+1):
        if arr[j] == 'G':
            cnt += 1
        elif arr[j] == 'H':
            cnt += 2
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
