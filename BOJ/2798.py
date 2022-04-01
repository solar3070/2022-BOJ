from itertools import combinations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

max_sum = 0
for it in combinations(lst, 3):
  if max_sum < sum(it) <= m:
    max_sum = sum(it)
    
print(max_sum)