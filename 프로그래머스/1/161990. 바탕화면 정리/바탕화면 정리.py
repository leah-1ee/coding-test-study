# 빈칸 . 파일 있는 칸 #
# 점 S(lux, luy)에서 점 E(rdx, rdy)
# 드래그 한 거리는 |rdx - lux| + |rdy - luy|로 정의
# 한 번 드래그, 최소거리
# [lux, luy, rdx, rdy]를 return
# 최소 위i, 최소 왼j, 최대아래i, 최대오 j


def solution(wallpaper):
    x_list = []
    y_list = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                x_list.append(i)
                y_list.append(j)
                
    # x중 제일 작은거, y중 제일 작은거, x중 제일 큰거+1, y중 제일 큰거+1
    return [min(x_list), min(y_list), max(x_list) + 1, max(y_list) + 1]