word1 = input()
word2 = input()
word3 = input()

len1 = len(word1)
len2 = len(word2)
len3 = len(word3)

longest = max(len1, len2, len3)
shortest = min(len1, len2, len3)

print(longest-shortest)