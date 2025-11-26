N, M = map(int, input().split())
arr = [input() for _ in range(N)]

# Please write your code here.
# arr[r][c]
# 상하좌우 좌상 좌하 우상 우하 
r_dir = [-1, 1, 0, 0, -1, 1, -1, 1]
c_dir = [0, 0, -1, 1, -1, -1, 1, 1]

# 'LEE' 완성 여부 체크 
def is_lee(r, c):
    # 완성 여부, 완성 개수 체크 
    flag = False
    subtotal = 0

    # 8 방향 체크 
    for dir_num in range(8):
        
        nr = r + r_dir[dir_num]
        nc = c + c_dir[dir_num]

        # 'EE' 체크 
        for _ in range(2):
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'E':
                nr += r_dir[dir_num]
                nc += c_dir[dir_num]

            # 미발견 시 break 
            else:
                break

        # 발견 시 True, 개수 + 1
        else:
            flag = True
            subtotal += 1 

    return flag, subtotal


def solution():
    # 총 LEE 개수 
    cnt = 0
    for i in range(N):
        for j in range(M):

            # L 발견되면 시작 
            if arr[i][j] == 'L':
                flag, subtotal = is_lee(i, j)

                # LEE 완성 시 개수 업데이트 
                if flag:
                    cnt += subtotal

    print(cnt)

solution()