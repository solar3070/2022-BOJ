from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))

op_lst = ['+'] * op_cnt[0] + ['-'] * op_cnt[1] + ['*'] * op_cnt[2] + ['/'] * op_cnt[3]

max_n = -1e9
min_n = 1e9

def calcExp(op):
  global max_n, min_n
  result = nums[0]

  for i in range(n - 1):
    if op[i] == '+':
      result += nums[i + 1]
    elif op[i] == '-':
      result -= nums[i + 1]
    elif op[i] == '*':
      result *= nums[i + 1]
    else:
      result = result // nums[i + 1] if result >= 0 else -(abs(result) // nums[i + 1])

  max_n = max(result, max_n)
  min_n = min(result, min_n)

for operator in permutations(op_lst, n - 1):
  calcExp(list(operator))

print(max_n, min_n, sep="\n")