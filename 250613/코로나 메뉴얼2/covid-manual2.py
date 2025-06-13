arr = [0]*4 

# 증상과 체온 입력 받아서 진료소 구분 
for i in range(3):
    sym, degree = input().split()
    degree = int(degree)

    if (sym=='Y') and (degree>=37):
        arr[0] += 1
    elif (sym=='N') and (degree>=37):
        arr[1] += 1
    elif (sym=='Y') and (degree<37):
        arr[2] += 1
    else:
        arr[3] += 1


print(' '.join(map(str, arr)), end=' ')

# 진료소 A 둘 이상이면 E 출력 
if arr[0] >= 2:
    print('E')