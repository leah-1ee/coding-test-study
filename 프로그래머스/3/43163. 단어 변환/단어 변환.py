from collections import deque 

def is_one_diff(a, b):
    diff = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            
        if diff > 1:
            return False
    
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)]) 
    visited = set()
    
    while queue: 
        now, depth = queue.popleft()
        
        if now == target:
            return depth
        
        for word in words:
            if word not in visited and is_one_diff(now, word):
                visited.add(word)
                queue.append((word, depth + 1))
    
    return 0