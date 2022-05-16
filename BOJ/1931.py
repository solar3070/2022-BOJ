import sys
input = sys.stdin.readline
n = int(input())
conf_info = []
for _ in range(n):
  conf_info.append(list(map(int, input().split())))

conf_info.sort(key = lambda x: (x[1], x[0]))

max_conf = 1
end = conf_info[0][1]
for i in range(1, n):
  if conf_info[i][0] >= end:
    max_conf += 1
    end = conf_info[i][1]

print(max_conf) 