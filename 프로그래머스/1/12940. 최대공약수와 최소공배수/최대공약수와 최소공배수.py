def solution(n, m):
    answer = []
    
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
        
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
        
    return answer

# math 라이브러리 이용 
# 최대공약수(gcd) 함수: math.gcd(a, b)
# 최소공배수(lcm): a*b // gcd

import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = n * m // gcd
        
    return [gcd, lcm]
