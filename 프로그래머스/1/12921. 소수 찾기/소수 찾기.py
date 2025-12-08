# 에라토스테네스의 체 활용 
def solution(n):
    # 모든 수가 소수라고 가정, 0,1은 제외 
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    
    # 2 ~ sqrt(n) 반복 
    for i in range(2, int(n**0.5)+1):
        # i가 소수이면 
        if sieve[i] == True:
            # i의 배수 전부 지움  
            for j in range(i*i, n+1, i):
                sieve[j] = False
                
    
    return sieve.count(True)