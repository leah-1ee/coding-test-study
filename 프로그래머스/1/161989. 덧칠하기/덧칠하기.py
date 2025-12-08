# 1 ~ n번 벽
# 롤러 사이즈 m

def solution(n, m, sections):
     
    cnt = 0     # 페인트칠 횟수
    painted = 0 # 롤러가 닿은 마지막 위치
    
    
    for section in sections:
        # 마지막으로 페인트를 칠한 구역 |  | 목표 구역(안 칠해짐)
        if painted < section:
            # 페인트칠
            cnt += 1
            # 마지막으로 칠해진 구역 기록 
            painted = section + m - 1
   
    return cnt