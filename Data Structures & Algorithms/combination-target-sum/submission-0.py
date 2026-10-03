class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def dfs(i):
            sub_sum = sum(sub)
            if i >= len(nums) or sub_sum>target:
                return
            if sub_sum == target:
                res.append(sub.copy())
                return

            sub.append(nums[i])
            dfs(i)

            sub.pop()
            dfs(i+1)
        
        dfs(0)
        return res