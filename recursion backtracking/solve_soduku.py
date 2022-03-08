def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    solve(board)


def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for k in range(1, 10):
                    if isValid(board, i, j, k):
                        board[i][j] = str(k)
                        if solve(board):
                            return True
                        else:
                            board[i][j] == "."
                return False
    return True


def isValid(board, row, col, value):
    for i in range(9):
        if board[row][i] == str(value):
            return False
        if board[i][col] == str(value):
            return False
        if board[3*int(row/3) + int(i/3)][3*int(col/3) + i % 3] == str(value):
            return False

    return True

print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
