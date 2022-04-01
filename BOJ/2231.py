def digit_sum(n):
  sum = n
  while n > 0:
    sum += n % 10
    n //= 10
  return sum

n = int(input())

digit = len(str(n))
front = n // 10 ** (digit - 2) - 1 if digit > 2 else n // 10 - 1

while digit_sum(front * 10 + 9) > n:
  front -= 1
start = front * 10 + 9

min_ctor = 0
for i in range(start, n):
  if digit_sum(i) == n:
    min_ctor = i
    break

print(min_ctor)