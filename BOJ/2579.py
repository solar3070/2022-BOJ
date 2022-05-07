import sys
n = int(input())
s = [int(sys.stdin.readline()) for _ in range(n)]

dp = []
for i in range(2):
  dp.append(sum(s[:i + 1])) 
if n >= 3:
  dp.append(max(s[0] + s[2], s[1] + s[2]))
for i in range(3, n):
  dp.append(max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i]))

print(dp)  
print(dp.pop())