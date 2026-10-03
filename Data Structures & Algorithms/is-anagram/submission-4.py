class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {'':0}
        for ch in s:
            anagram[ch] = anagram.get(ch,0) + 1
        
        for ch in t:
            if ch not in anagram:
                return False
            anagram[ch]-=1
        
        for val in anagram.values():
            if val!=0:
                return False
        return True