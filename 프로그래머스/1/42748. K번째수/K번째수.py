def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        # 1. 자르고 정렬 
        temp = sorted(array[i-1:j])
        # 2. k번째 수 구하기 
        answer.append(temp[k-1])
    
    return answer