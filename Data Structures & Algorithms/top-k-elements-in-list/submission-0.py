class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = [[] for _ in nums]

        count = defaultdict(int)

        for num in nums:
            count[num]+=1

        for i, j in count.items():
            freq[j-1].append(i)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                if k>0:
                    res.append(n)
                    k-=1
        
        return res
