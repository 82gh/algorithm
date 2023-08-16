board = []
for i in range(19):
    board.append([])
    for j in range(19):
        board[i].append(0)


num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

for i in range(19):
    for j in range(19):
        print(board[i][j],end =" ")
    print()
