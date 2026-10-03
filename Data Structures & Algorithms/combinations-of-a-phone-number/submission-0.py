class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        res = []
        def dfs(num, cur_s):
            if num == len(digits):
                res.append(cur_s)
                return
                
            for ch in hashmap[digits[num]]:
                dfs(num+1,cur_s+ch)
        
        dfs(0, '')
        return res