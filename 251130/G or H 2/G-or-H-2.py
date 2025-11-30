n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.
# 위치 별 알파벳 기록 
arr = [0] * (max(pos) + 1)

for i in range(n):
    arr[pos[i]] = alpha[i]

# 사진 최대 크기 저장 
max_pic = 0

# 사진 크기 결정 
# 사진 시작점 결정, 사람 없으면 다음 시작점으로 
for i in range(len(arr)):
    if arr[i] == 0:
        continue 
    # 사진 끝점 결정, 사람 없으면 다음 끝점으로 
    for j in range(i, len(arr)):
        if arr[j] == 0:
            continue 

        # 알파벳 수 세기 
        g_num = 0
        h_num = 0
        for k in range(i, j+1):
            if arr[k] == 'G':
                g_num += 1
            elif arr[k] == 'H':
                h_num += 1

        # 알파벳 수가 같거나, 한 가지 알파벳으로만 구성되어 있는 경우
        if (g_num == h_num and g_num >0 and h_num >0) or (g_num == 0 and h_num >0) \
        or (h_num == 0 and g_num > 0):
            # 사진 크기 업데이트 
            pic = j - i 
            max_pic = max(max_pic, pic)


print(max_pic)        