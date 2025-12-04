def solution(numbers):
    answer = set()
    n = len(numbers)
    
    # 두 수를 뽑는 모든 조합 탐색 
    for i in range(n-1):
        for j in range(i+1, n):
            answer.add(numbers[i] + numbers[j])
    
    
    return sorted(answer)