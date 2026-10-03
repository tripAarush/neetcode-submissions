class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            alph = [0] * 26
            for ch in strs[i]:
                alph[ord(ch)-ord('a')] += 1
            hashmap[tuple(alph)].append(strs[i])
        
        res = [x for x in hashmap.values()]
        return res
        
        # from collections import defaultdict
        # anag = defaultdict(list)
        # for i in range(len(strs)):
        #     st1 = "".join(sorted(strs[i]))
        #     anag[st1].append(strs[i])

        # res = [x for x in anag.values()]
        # return res
