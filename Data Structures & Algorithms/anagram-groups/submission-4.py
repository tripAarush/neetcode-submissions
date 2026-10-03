class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for st in strs:
            ord_list = [0]*26
            for ch in st:
                ord_list[ord(ch)-ord('a')]+=1
            hashmap[tuple(ord_list)].append(st)
        return list(hashmap.values())

        hashmap = defaultdict(list)
        for st in strs:
            hashmap["".join(sorted(st))].append(st)
        
        return list(hashmap.values())