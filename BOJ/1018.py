import sys

def count(board, x, y, color):
  count = 0
  for i in range(x, x + 8):
    for j in range(y, y + 8):
      if board[i][j] != color: count += 1 
      if j != y + 7:
        color = 'B' if color == 'W' else 'W'
  return count

n, m = map(int, input().split())
board = [0] * n
for i in range(n):
  board[i] = list(sys.stdin.readline())
  
min_cnt = n * m
for x in range(n - 8 + 1):
  for y in range(m - 8 + 1):
    b_cnt = count(board, x, y, 'B') 
    w_cnt = count(board, x, y, 'W')
    cnt = b_cnt if b_cnt < w_cnt else w_cnt
    if cnt < min_cnt:
      min_cnt = cnt

print(min_cnt)