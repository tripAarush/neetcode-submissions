class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(row,taken,queens):
            if row == n:
                res.append(queens.copy())
                return

            available = False
            for t in taken[row]:
                if t == 0:
                    available = True
            if not available:
                return

            for c, t in enumerate(taken[row]):
                if t == 0:
                    changed = set()
                    for r in range(n):
                        if taken[r][c] != 1:
                            changed.add((r,c))
                            taken[r][c] = 1

                    st = min(row,c)
                    st_row, st_col = row-st, c-st

                    while st_row < n and st_col < n:
                        if taken[st_row][st_col] != 1:
                            changed.add((st_row,st_col))
                            taken[st_row][st_col] = 1
                        st_row+=1
                        st_col+=1

                    st_row, st_col = row, c
                    while st_row < n and st_col >= 0:
                        if taken[st_row][st_col] != 1:
                            changed.add((st_row,st_col))
                            taken[st_row][st_col] = 1
                        st_row+=1
                        st_col-=1
                        
                    q = ''
                    for i in range(n):
                        q+='.' if i!=c else 'Q'
                    queens.append(q)
                    dfs(row+1, taken, queens)
                    
                    queens.pop()
                    for r, c in changed:
                        taken[r][c] = 0
        
        taken = [[0 for _ in range(n)] for _ in range(n)]
        dfs(0,taken,[])

        return res
