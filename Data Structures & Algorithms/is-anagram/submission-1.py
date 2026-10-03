class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = sorted(s)
        sort_t = sorted(t)
        if (sort_t == sort_s):
            return True
        else: return False
        