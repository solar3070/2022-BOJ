import sys

while True:
  a, b = map(int, sys.stdin.readline().split())
  if a == 0 and b == 0:
    break

  if b % a == 0: 
    print(b // a)
    print("factor")
  elif a % b == 0:
    print("multiple")
  else:
    print("neither")
