def solution(s):
    
    num = list(map(int, s.split()))
    
    return f'{min(num)} {max(num)}'