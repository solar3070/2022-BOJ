import sys
n = int(input())

cnt = [0] * (10001)
for i in range(n):
  cnt[int(sys.stdin.readline())] += 1

# for i in range(1, 10001):
#   if cnt[i - 1] != 0 and cnt[i] != 0:
#     cnt[i] += cnt[i - 1]
#     tmp = cnt[i]
#   elif cnt[i] != 0:
#     cnt[i] += tmp
#     tmp = cnt[i]

for i in range(10001):
  if cnt[i] != 0:
    for _ in range(cnt[i]):
      print(i)