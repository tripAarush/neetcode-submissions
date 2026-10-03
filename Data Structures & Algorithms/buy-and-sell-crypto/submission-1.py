class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_d = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l=r
                r+=1
                continue
            else:
                max_d = max(max_d, prices[r]-prices[l])
                r+=1
        
        return max_d
            