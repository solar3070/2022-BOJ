n = int(input())

board = [0] * n
cnt = 0

def check_board(idx):
  for i in range(idx):
    if board[idx] == board[i] or board[idx] + idx == board[i] + i or board[idx] - idx == board[i] - i:
      return False
  return True

def set_queen(idx):
  global cnt
  if idx == n:
    cnt += 1
    return

  for i in range(n):
    board[idx] = i
    if check_board(idx):
      set_queen(idx + 1)

set_queen(0)
print(cnt)