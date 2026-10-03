class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, j, k):
            if i not in range(len(board)) or j not in range(len(board[0])) or k>=len(word) or (i,j) in visited:
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word)-1 and board[i][j] == word[k]:
                return True
            
            visited.add((i,j))
            res = dfs(i,j+1,k+1) or dfs(i+1,j,k+1) or dfs(i,j-1,k+1) or dfs(i-1,j,k+1)

            visited.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True

        return False
