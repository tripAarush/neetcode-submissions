class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # seen set which has all the cordinates already checked
        # recrusively check for adjacent 1s, if not found then next coord
        import collections
        if not grid:
            return 0

        seen = set()
        num_islands = 0
        rows, cols = len(grid), len(grid[0])

        # def bfs(row, col):
        #     seen.add((row, col))
        #     q = collections.deque()
        #     q.append((row, col))
        #     while q:
        #         r, c = q.popleft()
        #         directions = [[1,0], [0,1], [-1,0], [0,-1]]
        #         for dr, dc in directions:
        #             if (r+dr in range(rows) and c+dc in range(cols) and
        #                 (r+dr, c+dc) not in seen and
        #                 grid[r+dr][c+dc]== '1'):
        #                 q.append((r+dr, c+dc))
        #                 seen.add((r+dr, c+dc))
        def dfs(row, col):
            seen.add((row,col))
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            for dr, dc in directions:
                if (row+dr in range(rows) and col+dc in range(cols)
                    and grid[row+dr][col+dc] == '1' 
                    and (row+dr, col+dc) not in seen):
                    dfs(row+dr, col+dc)

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in seen and grid[i][j] == '1':
                    dfs(i, j)
                    num_islands += 1
        
        return num_islands