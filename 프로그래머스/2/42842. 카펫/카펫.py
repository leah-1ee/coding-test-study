def solution(brown, yellow):

    b = int(brown/2) - 2
    y = yellow
    n = int((b+(b**2 - 4*y)**0.5) / 2) + 2
    m = int((b-(b**2 - 4*y)**0.5) / 2) + 2
    
    return [n, m]