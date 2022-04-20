n = int(input())
lst = [int(input()) for _ in range(n)]

def fibo(n):
  if n == 0 or n == 1:
    return n
  if memo[n - 1] == 0: 
    memo[n - 1] = fibo(n - 1)
  if memo[n - 2] == 0:
    memo[n - 2] = fibo(n - 2)
  return memo[n - 1] + memo[n - 2]

for n in lst:
  if n == 0:
    print("1 0")
  elif n == 1:
    print("0 1")
  else:
    memo = [0] * n
    cnt_1 = fibo(n)
    cnt_0 = memo[n - 1]
    print(cnt_0, cnt_1, sep=" ")