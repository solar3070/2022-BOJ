import sys
input = sys.stdin.readline
s = input()
q = int(input())

for _ in range(q):
  a, l, r = input().split()
  tmp = s[int(l) : int(r) + 1]
  print(tmp.count(a))