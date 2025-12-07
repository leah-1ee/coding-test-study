def solution(answers):
    
    # 찍기 패턴 
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 점수 
    scores = [0, 0, 0]
    
    # 점수 계산 
    # i: 정답인덱스, answer: 정답 번호 
    for i, answer in enumerate(answers):
        
        # 패턴 하나씩 탐색 
        # j: 패턴 번호, pattern: 패턴 리스트 
        for j, pattern in enumerate(patterns):
            
            # 정답 인덱스(i)가 패턴 길이를 넘어가면 다시 패턴 0번 인덱스부터 시작
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
                
    # 최다 정답자 번호 (1번부터 시작) 
    return [i+1 for i, score in enumerate(scores) if score == max(scores)]