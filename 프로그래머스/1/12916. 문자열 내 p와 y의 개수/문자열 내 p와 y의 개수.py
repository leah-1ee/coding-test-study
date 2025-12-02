def solution(s):
    
    num_p = 0
    num_y = 0
    
    s = s.lower()
    for c in s:
        if c == 'p':
            num_p += 1
        elif c == 'y':
            num_y += 1
    

    return True if num_p == num_y else False