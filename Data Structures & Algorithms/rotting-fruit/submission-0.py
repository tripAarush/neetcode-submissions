class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque()

        count, check = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2 or grid[i][j]==1:
                    count+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    check+=1

        res = 0
        while queue:
            res+=1
            for _ in range(len(queue)):
                rot_r, rot_c = queue.popleft()
                diff = [(0,-1),(0,1),(1,0),(-1,0)]
                for dr, dc in diff:
                    if rot_r+dr in range(len(grid)) and rot_c+dc in range(len(grid[0])) and grid[rot_r+dr][rot_c+dc] == 1:
                        queue.append((rot_r+dr,rot_c+dc))
                        check+=1
                        grid[rot_r+dr][rot_c+dc] = 2
        print(count,check)
        if check == count and check == 0:
            return 0
        if check == count:
            return res-1
        return -1
                    
