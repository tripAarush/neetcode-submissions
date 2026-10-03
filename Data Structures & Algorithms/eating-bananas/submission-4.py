class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        tot = float('inf')

        while high > low:
            mid = (high+low) // 2
            tot = 0
            for p in piles:
                tot += -(-p//mid)
            if tot > h:
                low = mid+1
            else:
                high = mid-1
    
        tot = 0
        for p in piles:
            tot+=-(-p//high)
        if tot > h:
            return high+1
        return high
        
