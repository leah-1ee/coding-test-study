def solution(k, m, score):
    
    # 점수 내림차순 정렬 
    score = sorted(score, reverse=True)
    # 최대 가격 
    price = 0
    
    
    for i in range(0, len(score), m):
        # 한 상자를 만들 수 있는지
        if (i+m) <= len(score):
            # 상자 구성 
            temp = score[i:i+m]
            # 가격 더하기 
            price += min(temp) * m
    
    
    return price