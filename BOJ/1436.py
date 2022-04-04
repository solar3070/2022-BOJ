def nth_number(n):
  order = 0
  start = 666
  while order != n:
    if "666" in str(start):
      order += 1
    start += 1
  return start - 1

n = int(input())
print(nth_number(n))