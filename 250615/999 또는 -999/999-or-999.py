lst = list(map(int, input().split()))
arr =[]

# 999나 -999 나오기 전까지 배열에 담기 
for n in lst:
    if n==999 or n==-999:
        break
    else:
        arr.append(n)

print(max(arr), end = ' ')
print(min(arr))