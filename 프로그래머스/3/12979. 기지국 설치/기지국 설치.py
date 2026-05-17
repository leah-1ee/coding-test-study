def solution(n, stations, w):
    length = 2 * w + 1
    cnt = 0
    
    coverage = [(0, 0)]
    for station in stations:
        coverage.append((station - w, station + w))
    coverage.append((n + 1, n + 1))
    
    for i in range(len(coverage) - 1):
        _, end = coverage[i]
        next_start, _ = coverage[i + 1]
        
        if end < next_start:
            not_covered = next_start - end - 1
            cnt += (not_covered + length - 1) // length
    
    return cnt