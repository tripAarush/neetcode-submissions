class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        left, right = 0, 0

        while right<len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                tot = max(tot, prices[right]-prices[left])
            right+=1
        
        return tot