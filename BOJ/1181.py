import sys
n = int(input())
word = [sys.stdin.readline().strip() for _ in range(n)]

word = list(set(word))
word.sort(key=len)
word.sort()

for w in word: print(w)