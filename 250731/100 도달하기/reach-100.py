n=int(input())

lst=[1, n]

for i in range(2, 100):
    lst.append(lst[i-1]+lst[i-2])
    if lst[-1]>100:
        break

for i in lst:
    print(i, end=" ")
