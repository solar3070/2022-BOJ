import sys
n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(len(lst) - 1):
  for j in range(len(lst) - i -1):
    if lst[j] > lst[j + 1]:
      lst[j], lst[j + 1] = lst[j + 1], lst[j]

for n in lst: print(n)