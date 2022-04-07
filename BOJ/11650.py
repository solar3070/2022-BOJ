import sys
n = int(input())
lst = []
for _ in range(n):
  lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort()
for a, b in lst:
  print(a, b)
