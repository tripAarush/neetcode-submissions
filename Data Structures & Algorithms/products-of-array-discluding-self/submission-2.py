class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        prefix = 1
        for i in range(1, len(nums)):
            res.append(prefix*nums[i-1])
            prefix*=nums[i-1]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = postfix*res[i]
            postfix*=nums[i]
        
        return res

        # brute force
        res = []
        prod = 1
        zeroes = []
        for i, num in enumerate(nums):
            if num == 0:
                zeroes.append(i)
            else: prod *= num
        if len(zeroes) > 1:
            return [0] * len(nums)

        for i, num in enumerate(nums):
            if zeroes and zeroes[0] == i:
                res.append(prod)
            elif not zeroes:
                res.append(prod//num)
            else:
                res.append(0)
        
        return res