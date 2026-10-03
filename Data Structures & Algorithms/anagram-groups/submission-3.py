class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for st in strs:
            hashmap["".join(sorted(st))].append(st)
        
        return list(hashmap.values())