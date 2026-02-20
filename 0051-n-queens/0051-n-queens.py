class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set() # store which col has queen
        diag1 = set() # row - col
        diag2 = set() # row + col
        queens = [-1] * n #queens[row] = col 
        res = []
        
        def backtrack(row):
            if row == n:
                temp = []
                for r in range(n):
                    temp.append('.' * queens[r] + 'Q' + '.' * (n - 1 - queens[r]))
                res.append(temp)
                return
            for col in range(n):
                #pruning
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                #backtracking
                
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
                
            
                
                
        
        