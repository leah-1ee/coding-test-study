def solution(babbling):
    answer = 0
    
    # 가능한 발음 리스트 
    available = ["aya", "ye", "woo", "ma"]
    
    # 주어진 단어에 대해 
    for word in babbling:
        # 연속된 발음이 있는지 검사 
        repeated = False
        
        for sound in available:
            if sound*2 in word:
                repeated = True
                break
        
        # 연속된 발음이 있다면 다음 단어로 
        if repeated:
            continue
        
        # 발음 가능한 부분을 공백으로 치환 
        # 빈 문자열로 치환하면 남은 글자가 합쳐져서 발음 가능한 단어가 될 수 있음 
        for sound in available:
                word = word.replace(sound, " ")
                
        # 공백 제거, 남는 글자가 없으면 발음 가능함 
        if word.strip() == "":
            answer += 1
                         
    return answer