class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        sort_strs = []

        for st in strs:
            sort_strs.append("".join(sorted(st)))

        hashmap = defaultdict(list)
        for idx, st in enumerate(sort_strs):
            hashmap[st].append(strs[idx])
        
        return list(hashmap.values())