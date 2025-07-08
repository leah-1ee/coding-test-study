# park에서 -1만 있는 정사각형 찾기
# 가장 큰 정사각형부터 시도

# 1. 가장 큰 돗자리부터 park 전체에 시도
# 2. 각 위치 [i, j]에서 size x size 가능한지 확인
# 3. 가능하면 리턴, 안 되면 다음 크기로

# 돗자리가 들어갈 수 있는지 확인
def can_place(park, i, j, size):
    # i, j 를 시작점으로 size x size 가능?
    for x in range(i, i + size):
        for y in range(j, j + size):
            if x >= len(park) or y >= len(park[0]):
                return False  # 범위 벗어남
            if park[x][y] != "-1":
                return False  # 사람 있음
    return True

def solution(mats, park):
    # 가장 큰 정사각형부터 시도
    mats.sort(reverse=True)

    for size in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if can_place(park, i, j, size):
                    return size  # 가장 큰 크기 먼저 리턴!
    return -1
