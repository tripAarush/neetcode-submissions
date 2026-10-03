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
                if mid-1>=0:
                    tot = 0
                    for p in piles:
                        tot+=-(-p//(mid-1))
                    if tot > h:
                        return mid
                high = mid-1
        return high
        
