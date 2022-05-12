import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin_lst = []
for _ in range(n):
  coin_lst.insert(0, int(input()))

coin_cnt = 0
for coin in coin_lst:
  if k == 0:
    break
  elif k // coin >= 1:
    coin_cnt += k // coin
    k %= coin

print(coin_cnt)