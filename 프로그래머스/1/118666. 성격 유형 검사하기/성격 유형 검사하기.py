def solution(survey, choices):
    answer = ''
    
    # 성격 유형별 점수를 저장하는 딕셔너리 
    personality = {k:0 for k in 'RTCFJMAN'}
    
    # 성격 유형 점수 계산 
    for char, num in zip(survey, choices):
        if num == 4:
            continue
        elif num < 4:
            personality[char[0]] += (4-num)
        else:
            personality[char[1]] += (num-4)
    
    # 결과 산출
    # 비교해야 할 지표를 미리 정의 
    indicators = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for type1, type2 in indicators:
        if personality[type1] >= personality[type2]:
            answer += type1
        else:
            answer += type2
    
    return answer