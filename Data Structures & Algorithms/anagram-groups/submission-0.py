class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anag = defaultdict(list)
        for i in range(len(strs)):
            st1 = "".join(sorted(strs[i]))
            anag[st1].append(strs[i])

        res = [x for x in anag.values()]
        return res
