import sys
n = int(input())
word = [sys.stdin.readline().strip() for _ in range(n)]

word = list(set(word))
word.sort(key=len)

length = 1
tmp, result = [], []
for w in word:
  if len(w) != length:
    length = len(w)
    tmp.sort()
    result += tmp
    tmp = [w]
  else:
    tmp.append(w) 
tmp.sort()
result += tmp

for word in result: print(word)