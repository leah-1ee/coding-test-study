def solution(s):
    
    # 문자 변환을 위해 리스트로 변환 
    s = list(s)
    # 단어 별 인덱스 저장 
    index = 0
    
    # 모든 문자 순회
    for i in range(len(s)):
        # 공백이면 새로운 단어 -> 인덱스 초기화
        if s[i] == ' ':
            index = 0
            continue
        # 짝수 번째 문자 -> 대문자 
        elif index % 2 == 0:
            s[i] = s[i].upper()
        # 홀수 번째 문자 -> 소문자 
        else:
            s[i] = s[i].lower()
        index += 1
    
    
    return ''.join(s)