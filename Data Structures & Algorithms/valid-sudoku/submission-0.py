class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            rows = set()
            col = set()
            for j in range(9):
                if board[i][j] in rows:
                    return False
                else:
                    if board[i][j] != '.':
                        rows.add(board[i][j])

                if board[j][i] in col:
                    return False
                else:
                    if board[j][i] != '.':
                        col.add(board[j][i])


        d= {}

        for i in range(9):
            for j in range(9):
                quadrante = (i // 3, j // 3)

                if board[i][j] == '.':
                    continue

                if quadrante in d:
                    if board[i][j] in d[quadrante]:
                        return False
                    else:
                        d[quadrante].append(board[i][j])

                else:
                    d[quadrante] = [board[i][j]]
                    

        return True