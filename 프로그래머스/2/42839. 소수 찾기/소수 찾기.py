from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
        
    return True

def solution(numbers):
    nums = set()
    
    for r in range(1, len(numbers)+1):
        nums.update(
            int(''.join(p))
            for p in permutations(numbers, r)
        )
    
    return sum(1 for n in nums if is_prime(n))