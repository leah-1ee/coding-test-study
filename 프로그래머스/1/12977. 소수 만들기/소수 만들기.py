from itertools import combinations

# 소수 판별 함수
def is_prime(num):

    if num < 2:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True


def solution(nums):

    cnt = 0
    
    # 3개 수 모든 조합 
    for comb in combinations(nums, 3):
        total = sum(comb)
        
        # 소수면 cnt +1
        if is_prime(total):
            cnt += 1

    return cnt