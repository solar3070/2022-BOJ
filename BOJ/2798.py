n, m = map(int, input().split())
lst = list(map(int, input().split()))

dif = 300000
for i in range(n - 2):
  for j in range(i + 1, n - 1):
    for k in range(j + 1, n):
      sum = lst[i] + lst[j] + lst[k]
      if m - sum < dif and sum <= m:
        dif = m - sum
        result = sum

print(result)