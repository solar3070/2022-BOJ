n = int(input())
trgl = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  for j in range(i + 1):
    if j == 0:
      trgl[i][j] += trgl[i - 1][j]
    elif j == i:
      trgl[i][j] += trgl[i - 1][j - 1]
    else:
      trgl[i][j] += max(trgl[i - 1][j], trgl[i - 1][j - 1])

print(max(trgl[n - 1]))