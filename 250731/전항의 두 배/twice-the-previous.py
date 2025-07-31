lst=list(map(int, input().split()))

result=[lst[0], lst[1]]

for i in range(2, 10):
    result.append(result[i-1]+result[i-2]*2)

for i in result:
    print(i, end=" ")