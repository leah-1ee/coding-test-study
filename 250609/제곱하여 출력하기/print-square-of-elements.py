n = int(input())
lst = list(map(int, input().split()))

# list comprehension 으로 제곱 
lst = [i**2 for i in lst]

print(' '.join(map(str,lst)))