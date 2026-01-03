def solution(s, skip, index):
    answer = ''
    
    # 문자열 s의 각 알파벳 alp에 대하여 
    for alp in s:
        # index 만큼 뒤의 알파벳으로 
        for _ in range(index):
            # 알파벳이 z를 넘어갈 경우 a로 
            if (ord(alp) + 1) > ord('z'):
                alp = 'a'
            # z 넘지 않으면 뒤의 알파벳으로 
            else:
                alp = chr(ord(alp) + 1)
            
            # skip을 벗어날 때까지 뒤로 한 칸씩
            while (alp in skip):
                if (ord(alp) + 1) > ord('z'):
                    alp = 'a'
                else:
                    alp = chr(ord(alp) + 1)
                    
        # 만들어진 알파벳 추가 
        answer += alp
                
    
    return answer