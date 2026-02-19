class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set() #record which col has the queen
        diag1 = set() #diag row - col
        diag2 = set() #diag row + col
        queens = [-1] * n #queens[row] = col record which col queens were put in each row

        def backtrack(row):
            if row == n:
                board = []
                for r in range(n):
                    board.append("." * queens[r] + "Q" + "." * (n - queens[r] - 1))
                res.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                queens[row] = col
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res
