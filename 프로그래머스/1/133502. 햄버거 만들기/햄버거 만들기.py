# 1231 -> 완성 

def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        # 재료 하나씩 쌓기 (push)
        stack.append(i)
        
        # 스택 끝 4개가 햄버거 패턴인지 확인
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            del stack[-4:]  # 햄버거 재료 4개 pop 
    
    return answer