class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # / diagonals have same row + col value and \ diagonals have same row - col value
        res = []
        cols = set()
        left_to_right = set()
        right_to_left = set()

        def dfs(row,queens):
            if row == n:
                res.append(queens.copy())
                return

            for col in range(n):
                if col not in cols and row - col not in left_to_right and row+col not in right_to_left:
                    cols.add(col)
                    left_to_right.add(row - col)
                    right_to_left.add(row+col)
                    queens.append("."*col + "Q" + "."*(n-1-col))

                    dfs(row+1, queens)

                    queens.pop()
                    cols.remove(col)
                    left_to_right.remove(row - col)
                    right_to_left.remove(row+col)

        dfs(0,[])

        return res
