def can_place(a, b, mat, park):
    for i in range(a, mat+a):
        for j in range(b, mat+b):
            if i >= len(park) or j >= len(park[0]) or park[i][j] != "-1":
                return -1
                
    return mat
                
        

def solution(mats, park):
    mats.sort(reverse = True)
    for mat in mats:
        for a in range(len(park)):
            for b in range(len(park[0])):
                available = can_place(a, b, mat, park)
                if available != -1:
                    return available
    return -1
        