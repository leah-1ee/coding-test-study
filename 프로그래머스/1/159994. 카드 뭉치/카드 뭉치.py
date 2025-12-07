def solution(cards1, cards2, goal):
    
    # 포인터 2개 초기화 
    idx1 = 0
    idx2 = 0
    
    # goal의 card를 하나씩 확인 
    for card in goal:
        # 현재 순서랑 card 일치하는지 확인, 일치하면 포인터 이동 
        if idx1 < len(cards1) and cards1[idx1] == card:
            idx1 += 1
            
        elif idx2 < len(cards2) and cards2[idx2] == card:
            idx2 += 1
        # 순서가 안 맞거나 없는 단어 -> No
        else:
            return "No"
    
    return "Yes"