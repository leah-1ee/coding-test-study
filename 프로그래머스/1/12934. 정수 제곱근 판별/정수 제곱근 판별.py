def solution(n):
    sqrt = n ** 0.5
    
    return (sqrt + 1) ** 2 if sqrt.is_integer() else -1