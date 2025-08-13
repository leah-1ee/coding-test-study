def solution(data, ext, val_ext, sort_by):
    table_map = {"code":0, "date":1, "maximum":2, "remain":3}
    
    ext_index = table_map.get(ext)
    sortby_index = table_map.get(sort_by)
    
    
    answer = [d for d in data if d[ext_index] < val_ext]
    
    answer.sort(key = lambda x: x[sortby_index])
    
    return answer
