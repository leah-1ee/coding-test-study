def solution(n, lost, reserve):
    
    both = set(lost) & set(reserve)
    
    lost = set(lost) - both
    reserve = set(reserve) - both
    
    for person in sorted(reserve):
        if person - 1 in lost:
            lost.remove(person - 1)
        elif person + 1 in lost:
            lost.remove(person + 1)
    
    return n - len(lost)