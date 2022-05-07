import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pfs = list(map(int, input().split()))

for i in range(1, n):
  pfs[i] += pfs[i - 1]
pfs = [0] + pfs # pfs.insert(0, 0)

for _ in range(m):
  i, j = map(int, input().split())
  print(pfs[j] - pfs[i - 1])