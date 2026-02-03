# 1등부터 등수 순서대로 배열에 담아 return
def solution(players, callings):
    
    # 이름:등수 를 저장하는 딕셔너리
    rank = {name:i for i, name in enumerate(players)}
    
    for name in callings:
        # 추월한 이름의 등수 
        current_rank = rank[name]
        
        # 추월 당한 등수, 이름
        front_rank = current_rank - 1
        front_player = players[front_rank]
        
        # players 배열에서 위치 swap
        players[current_rank], players[front_rank] = players[front_rank], players[current_rank]
        
        # 딕셔너리 등수 업데이트 
        rank[name] -= 1
        rank[front_player] += 1
    
    return players