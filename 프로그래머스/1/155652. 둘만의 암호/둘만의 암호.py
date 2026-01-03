from string import ascii_lowercase
def solution(s, skip, index):
    answer = ''
    
    # 전체 알파벳에서 skip 제외한 알파벳 배열 생성 
    valid_alpha = [char for char in ascii_lowercase if char not in skip]
    
    for char in s:
        # 현재 문자 위치 찾음
        curr_pos = valid_alpha.index(char)
        
        # index 만큼 이동, 리스트 순회 
        new_pos = (curr_pos + index) % len(valid_alpha)
        
        # 변환 완료된 알파벳 정답 문자열에 추가 
        answer += valid_alpha[new_pos]

    return answer