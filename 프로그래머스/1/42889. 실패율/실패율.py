# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# stage_dict key:i, value:fail_rate 

def solution(N, stages):
    # 스테이지 별 실패율 저장 
    stage_dict = {}
    
    for i in range(1, N+1):
        # 실패율 구하기 
        player = 0
        not_clear = 0
        
        for stage in stages:
            # 스테이지에 도달한 플레이어 수
            if i <= stage:
                player += 1
            # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
            if i == stage:
                not_clear += 1
        
        # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
        if player:
            fail_rate = not_clear/player 
        else:
            fail_rate = 0
        
        # 딕셔너리 저장
        stage_dict[i] = fail_rate
        
    # 정렬 기준: 1. 실패율 높은 순, 2. 스테이지 번호 작은 순 
    sorted_dict = sorted(stage_dict, key = lambda x: (-stage_dict[x], x))
    
    return sorted_dict 