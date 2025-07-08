def solution(arr):
    minimum = min(arr)
    arr.remove(minimum)
    
    if arr:
        return arr
    else:
        return [-1]