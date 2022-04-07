import statistics, sys
n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]

print(round(statistics.mean(lst)))
print(statistics.median(lst))
mode = statistics.multimode(lst)
if len(mode) > 1:
  mode.sort()
  print(mode[1])
else:
  print(mode[0])
print(max(lst) - min(lst))