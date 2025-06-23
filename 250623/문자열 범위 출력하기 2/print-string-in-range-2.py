word = input()
n = int(input())


for elem in word[:len(word)-n-1:-1]:
    print(elem, end="")