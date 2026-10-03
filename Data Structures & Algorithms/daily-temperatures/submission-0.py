class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                last_temp, last_idx = stack.pop()
                hashmap[last_idx] = idx-last_idx
            stack.append((temp, idx))
        
        for key, val in hashmap.items():
            res[key] = val
        
        return res
