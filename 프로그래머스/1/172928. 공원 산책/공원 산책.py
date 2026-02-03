# 방향 거리
# 벗어나는지? 장애물? -> 다음명령 수행

def solution(park, routes):
    
    # 방향 결정 
    dir_num = {'N':0, 'S':1, 'W':2, 'E':3}
    dir_r = [-1, 1, 0, 0]
    dir_c = [0, 0, -1, 1]
    
    # 공원 크기 측정 
    h = len(park)
    w = len(park[0])
    
    # 시작 지점 결정 
    for r in range(h):
        for c in range(w):
            if park[r][c] == 'S':
                cur_r = r
                cur_c = c
                break
    
    for route in routes:
        # 방향, 거리 저장 
        direction, dist = route.split()
        dist = int(dist)
        
        di = dir_num[direction]
        next_r = cur_r 
        next_c = cur_c 
        
        # 거리만큼 반복 
        for _ in range(dist):
            # 방향으로 한 칸 전진 
            next_r += dir_r[di]
            next_c += dir_c[di]
        
            # 조건 검사 1: 공원을 벗어나는지
            if not (0 <= next_r and next_r < h and 0 <= next_c and next_c < w):
                break
            # 조건 검사 2: 이동 중 장애물을 만나는지
            elif park[next_r][next_c] == 'X':
                break
                
        # 조건 만족하지 않을 시 이동        
        else:
            cur_r = next_r
            cur_c = next_c
    
    
    return [cur_r, cur_c]