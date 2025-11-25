board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.
# 19 x 19
# 검 1 흰 2 없음 0
# 가운데 위치 알: 가로 세로 출력


# 승리자 결정 여부 
win = False 

# 승리했는지 판별 
def is_win(c, r, num):
    # 하 우 우상 우하  방향 바둑알 체크 
    c_dir = [0, 1, 1, 1]
    r_dir = [1, 0, -1, 1]

    # 4방향 탐색 
    for dir_num in range(4):
        nc, nr = c + c_dir[dir_num], r + r_dir[dir_num]

        # 시작점 제외 4개 알이 연속으로 놓여 있으면 승리 
        for _ in range(4): 
            # 범위 0 ~ 18, 바둑알 값 체크 
            if 0 > nr or nr >= 19 or 0 > nc or nc >= 19 or board[nc][nr] != num:
                break 
 
            # 조건 만족 -> 다음 알 체크 
            else:
                nc += c_dir[dir_num]
                nr += r_dir[dir_num]

        # 승리 시 중앙 알 찾고 리턴 
        else:
            c = c + (c_dir[dir_num] * 2)
            r = r + (r_dir[dir_num] * 2)
            return True, c, r 

    # 승리 아닐 시 False 리턴 
    return False, 0, 0 

# 바둑판 전체에 대해서 
for i in range(19):
    for j in range(19):
        # 흰 바둑알 나왔을 경우 
        if board[i][j] == 1:
            start_c = i  
            start_r = j
            # 승리 여부 탐색 
            win, c, r = is_win(start_c, start_r, 1)
            # 승리 시 출력 후 탐색 종료 
            if win:
                print(1)
                print(f"{c+1} {r+1}")
                break

        # 검은 바둑알 나왔을 경우 
        elif board[i][j] == 2:
            start_c = i
            start_r = j
            # 승리 여부 탐색 
            win, c, r = is_win(start_c, start_r, 2)
            # 승리 시 출력 후 탐색 종료 
            if win:
                print(2)
                print(f"{c+1} {r+1}")
                break
    # 승리 시 반복 종료 
    if win:
        break
# 승리자 없을 시 0 출력 
else:
    print(0)
