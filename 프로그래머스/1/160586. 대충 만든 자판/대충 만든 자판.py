def solution(keymap, targets):
    answer = []   # 정답 배열
    key_dict = {} # 문자 : 누르는 횟수 저장 딕셔너리 
    
    # 문자 별 누르는 횟수 딕셔너리에 저장 
    for key in keymap:
        for char in key:
            # 처음 나온 문자 또는 최소 횟수가 아닌 문자면 업데이트 
            if (char not in key_dict) or (key_dict[char] > key.index(char)):
                key_dict[char] = key.index(char) + 1
                

    # 타겟 문자열 작성 가능 횟수 세기 
    for target in targets:
        cnt = 0
        for char in target:
            # 문자 입력 가능하면 횟수 세기 
            if char in key_dict:
                cnt += key_dict[char]
            # 문자 입력 불가능하면 -1  
            else:
                answer.append(-1)
                break
                
        # 모든 문자 입력 가능 시 누르는 횟수 기록 
        else:
            answer.append(cnt)
            
    
    return answer