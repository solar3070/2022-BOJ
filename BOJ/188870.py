import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

tmp = sorted(list(set(lst)))
dic = {tmp[i] : i for i in range(len(tmp))}

for n in lst:
  print(dic[n], end = " ")