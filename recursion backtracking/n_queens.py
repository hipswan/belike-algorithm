
def solveNQueens(n: int):
    board = ["."*n]*n
    leftRow = [0]*n
    lowerDiagonal = [0]*(2*n-1)
    upperDiagonal = [0]*(2*n-1)
    queens = []
    findQueens(0, board, queens, leftRow, lowerDiagonal, upperDiagonal, n)
    return queens


def findQueens(col, board, queens, leftRow, lowerDiagonal, upperDiagonal, n):
    if col == n:
        queens.append(list(board))
        return
    for row in range(n):
        if leftRow[row] == 0 and upperDiagonal[row+col] == 0 and lowerDiagonal[n-1+col-row] == 0:
            board[row] = board[row][:col]+"Q"+board[row][col+1:]
            leftRow[row] = 1
            upperDiagonal[row+col] = 1
            lowerDiagonal[len(board)-1+col-row] = 1
            findQueens(col+1, board, queens, leftRow,
                       lowerDiagonal, upperDiagonal, n)
            board[row] = board[row][:col]+"."+board[row][col+1:]
            leftRow[row] = 0
            upperDiagonal[row+col] = 0
            lowerDiagonal[len(board)-1+col-row] = 0

print(solveNQueens(4))