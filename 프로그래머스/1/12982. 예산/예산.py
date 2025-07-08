def solution(d, budget):
    d.sort()
    cnt = 0
    
    for n in d:
        if budget < n:
            break
        budget -= n
        cnt += 1
    
    return cnt
