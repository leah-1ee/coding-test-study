def solution(s):
    answer = 0 
    cnt_x = 0
    cnt_not_x = 0
    
    for char in s:
        # 새 분류 시작: x 지정 
        if cnt_x == 0 and cnt_not_x == 0:
            x = char
        
        # x와 같은 글자인지 다른 글자인지 카운트 
        if x == char:
            cnt_x += 1
        else:
            cnt_not_x += 1
        
        # 개수 같아지면 
        if cnt_x == cnt_not_x:
            # 분류 횟수 카운트
            answer += 1
            # 카운트 초기화 
            cnt_x, cnt_not_x = 0, 0
    
    # 문자열이 남아있으면 분류 횟수 + 1
    if cnt_x > 0:
        answer += 1

    
    return answer