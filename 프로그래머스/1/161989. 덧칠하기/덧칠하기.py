# 1 ~ n번 벽
# 롤러 사이즈 m

def solution(n, m, sections):
    # 페인트칠 횟수 기록 
    cnt = 0
    
    # 페인트가 칠해지지 않은 벽 False로 표시 
    wall = [True] * (n+1)
    for section in sections:
        wall[section] = False
        
    # 페인트칠이 필요한 영역에 대해
    for section in sections:
        if wall[section] == False:
            # 페인트칠 
            for i in range(section, section + m):
                # 범위 확인 
                if i <= n:
                    wall[i] = True
            # 페인트칠 횟수 증가 
            cnt += 1

    
    return cnt