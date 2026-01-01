# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# stage_dict key:i, value:fail_rate 

def solution(N, stages):
    # 스테이지 별 실패율 저장 
    stage_dict = {}
    
    # 전체 플레이어 수
    total_player = len(stages)
    
    for i in range(1, N+1):
        # 실패율 구하기 
        if total_player:
            # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
            player = stages.count(i)
            # 실패율 계산 
            fail_rate = player / total_player
            # 다음 스테이지에 도달한 플레이어 수 = 현재 인원 - 현재 스테이지에 멈춘 플레이어 수 
            total_player -= player
        
        # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0
        else:
            fail_rate = 0
            
        # 스테이지 번호 : 실패율 저장 
        stage_dict[i] = fail_rate
        
    # 정렬 기준: 1. 실패율 높은 순, 2. 스테이지 번호 작은 순 
    sorted_dict = sorted(stage_dict, key = lambda x: (-stage_dict[x], x))
    
    return sorted_dict 