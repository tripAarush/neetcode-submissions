class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        hashmap = defaultdict(int)
        hashmap1 = defaultdict(int)
        if (len(s)!=len(t)):
            return False

        for i in range(len(s)):
            hashmap[s[i]] += 1
            hashmap1[t[i]] += 1

        for stri in hashmap:
            if not hashmap1[stri] or hashmap1[stri] != hashmap[stri]:
                return False
        return True