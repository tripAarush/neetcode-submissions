class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res+=str(len(st))+"#"+st
        return res

    def decode(self, s: str) -> List[str]:
        idx = 0
        res = []
        while idx<len(s):
            leng = ""
            while s[idx]!="#":
                leng+=s[idx]
                idx+=1
            length = int(leng)
            res.append(s[idx+1:idx+length+1])
            idx = idx+length+1
        return res
