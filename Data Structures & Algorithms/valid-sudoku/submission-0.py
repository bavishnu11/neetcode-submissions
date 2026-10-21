class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in a:
                    return False
                a.add(board[i][j])

        for i in range(9):
            a = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in a:
                    return False
                a.add(board[j][i])

        for s in range(9):
            a = set()
            for i in range(3):
                for j in range(3):
                    r = (s//3) * 3 + i
                    c = (s % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in a:
                        return False
                    a.add(board[r][c])
        return True
                