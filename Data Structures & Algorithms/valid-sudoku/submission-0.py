class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # brute force: check possibilities
        rows,cols = len(board), len(board[0])

        #rows
        for j in range(cols):
            seen = set()
            blanks = 0
            for i in range(rows):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                else:
                    blanks+=1
            if len(seen) + blanks != 9:
                return False

        #cols
        for i in range(rows):
            seen = set()
            blanks = 0
            for j in range(cols):
                if board[i][j] != ".":
                    seen.add(board[i][j])
                else:
                    blanks+=1
            if len(seen) + blanks != 9:
                return False
        
        #3x3
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                blanks = 0
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j] != ".":
                            seen.add(board[i][j])
                        else:
                            blanks+=1
                if len(seen) + blanks != 9:
                    return False
        return True

