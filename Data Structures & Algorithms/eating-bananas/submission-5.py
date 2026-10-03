class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while high > low:
            mid = (high+low) // 2
            tot = 0
            for p in piles:
                tot += -(-p//mid)
            if tot > h:
                low = mid+1
            else:
                high = mid
    
        return high
        
