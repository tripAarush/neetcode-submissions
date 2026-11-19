class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        if len(board) < 2 or len(board[0]) < 2:
            return

        dir = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(row, col):
            if row not in range(len(board)) or col not in range(len(board[0])) or (row,col) in visited or board[row][col]=='X':
                return
            if board[row][col] == 'O':
                visited.add((row,col))
            
            for dr, dc in dir:
                dfs(row+dr, col+dc)
        
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][len(board[0])-1] == 'O':
                dfs(i,len(board[0])-1)
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[len(board)-1][j] == 'O':
                dfs(len(board)-1,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == 'O' and (i,j) not in visited):
                    board[i][j] = 'X'
        
