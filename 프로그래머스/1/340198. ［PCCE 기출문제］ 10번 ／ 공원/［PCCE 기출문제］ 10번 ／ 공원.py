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
    mats.sort(reverse=True)

    for size in mats:
        for i in range(len(park)):
            for j in range(len(park[0])):
                if can_place(park, i, j, size):
                    return size  # 가장 큰 크기 먼저 리턴!
    return -1
