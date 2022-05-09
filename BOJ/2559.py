import sys
input = sys.stdin.readline
n, k = map(int, input().split())
pfs = list(map(int, input().split()))

for i in range(1, n):
  pfs[i] += pfs[i - 1]

lst = []
for i in range(k, n):
  lst.append(pfs[i] - pfs[i - k])

if k == n: # 주의 케이스 1
  lst += [pfs[n - 1]]
elif k != 1: # 주의 케이스 2
  lst += [pfs[1]]
else:
  lst += [pfs[0]]

print(max(lst))