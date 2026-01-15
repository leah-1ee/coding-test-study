def solution(survey, choices):
    answer = ''
    
    # 성격 유형별 점수를 저장하는 딕셔너리 
    personality = {
        'R':0,
        'T':0,
        'C':0,
        'F':0,
        'J':0,
        'M':0,
        'A':0,
        'N':0
    }
    
    # 성격 유형 점수 계산 
    for char, num in zip(survey, choices):
        if num == 4:
            continue
        elif num < 4:
            personality[char[0]] += (4-num)
        else:
            personality[char[1]] += (num-4)
    
    # 유형 알파벳, 값을 각각 리스트로 만들기 
    key_list = list(personality.keys())
    value_list = list(personality.values())
    
    # 성격 유형 정의: 값이 큰 알파벳, 값이 같다면 순서가 먼저인 알파벳 
    i, j = 0, 1
    for _ in range(4):
        if value_list[i] > value_list[j]:
            answer += key_list[i]
        elif value_list[i] < value_list[j]:
            answer += key_list[j]
        else:
            answer += key_list[i] if key_list[i] < key_list[j] else key_list[j]
            
        i += 2
        j += 2
    
    return answer