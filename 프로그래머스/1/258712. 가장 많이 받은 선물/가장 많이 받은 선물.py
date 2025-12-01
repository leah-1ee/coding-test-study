# 1. 선물 더 많이 준 사람이 받음
# 2. 선물 x or 수 같음 -> 지수 높은 사람이 받음
# 지수 = 준 선물 - 받은 선물
# 지수까지 같으면 선물 x


def solution(friends, gifts):
    n = len(friends)
    
    # 1. 친구 이름 -> 인덱스 매핑 (Dictionary)
    friend_map = {name: i for i, name in enumerate(friends)}
    
    # 2. 주고받은 선물 표 (2차원 배열) & 선물 지수
    # gift_graph[i][j]: i가 j에게 준 선물 개수
    gift_graph = [[0] * n for _ in range(n)]
    gift_index = [0] * n # 선물 지수 (준 선물 - 받은 선물)
    
    # 3. 기록 채우기
    for gift in gifts:
        giver, receiver = gift.split() # "muzi frodo" -> 분리
        r = friend_map[giver]
        c = friend_map[receiver]
        
        gift_graph[r][c] += 1
        
        # 선물 지수 계산: 줄 때 +1, 받을 때 -1
        gift_index[r] += 1
        gift_index[c] -= 1
        
    # 4. 다음 달 받을 선물 계산
    get_gift = [0] * n
    
    # 모든 친구 쌍을 한 번씩만 비교 (조합)
    for i in range(n):
        for j in range(i + 1, n):
            # i가 j에게 준 것 vs j가 i에게 준 것
            give_i = gift_graph[i][j]
            give_j = gift_graph[j][i]
            
            if give_i > give_j:     # i가 더 많이 줬으면
                get_gift[i] += 1    # i가 받음
            elif give_i < give_j:   # j가 더 많이 줬으면
                get_gift[j] += 1    # j가 받음
            else:                   # 같거나 둘 다 안 준 경우 (0 == 0)
                # 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    get_gift[i] += 1
                elif gift_index[i] < gift_index[j]:
                    get_gift[j] += 1
                # 선물 지수까지 같으면 아무도 안 받음
                
    return max(get_gift)