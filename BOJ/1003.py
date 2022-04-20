n = int(input())
lst = [int(input()) for _ in range(n)]

def fibo(n):
  global cnt_0, cnt_1

  if n == 0:
    cnt_0 += 1
    return 0
  elif n == 1:
    cnt_1 += 1 
    return 1

  if memo[n - 1] == 0: 
    memo[n - 1] = fibo(n - 1)
  else:
    if n - 1 == 0:
      cnt_0 += 1
    elif n - 1 == 1:
      cnt_1 += 1
  if memo[n - 2] == 0:
    memo[n - 2] = fibo(n - 2)
  else:
    if n - 2 == 0:
      cnt_0 += 1
    elif n - 2 == 1:
      cnt_1 += 1

  return memo[n - 1] + memo[n - 2]

for n in lst:
  cnt_0 = cnt_1 = 0
  memo = [0] * n
  fibo(n)
  print(cnt_0, cnt_1, sep=" ")