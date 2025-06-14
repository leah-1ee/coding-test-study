arr = ['L', 'E', 'B', 'R', 'O', 'S']

letter = input()

# 배열에 문자가 있으면 인덱스 출력 
if letter in arr:
    print(arr.index(letter))
    
# 배열에 문자가 없으면 None 출력 
else:
    print("None")