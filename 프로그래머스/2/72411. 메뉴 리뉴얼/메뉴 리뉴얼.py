from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for r in course:
        counter = Counter()
        
        for order in orders:
            order = ''.join(sorted(order))
            
            for combo in combinations(order, r):
                counter[''.join(combo)] += 1
        
        if not counter:
            continue
        
        max_count = max(counter.values())

        if max_count >= 2:
            for menu, count in counter.items():
                if count == max_count:
                    answer.append(menu)
                    
    return sorted(answer)