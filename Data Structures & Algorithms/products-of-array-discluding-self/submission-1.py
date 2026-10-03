class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [0]*len(nums)

        for i in range(len(nums)):
            if i==0:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i]*prefix[i-1])
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i] = nums[i]
            else:
                postfix[i] = nums[i] * postfix[i+1]
        
        res = []
        for i in range(len(nums)):
            if i==0:
                res.append(postfix[i+1])
            elif i==len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        
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