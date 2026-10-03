class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq = [False] * 128
        count = [0] * 128
        for ch in t:
            freq[ord(ch)] = True
            count[ord(ch)] += 1
        left, right = 0, len(t)-1

        cur_count = [0] * 128
        cur_freq = [False] * 128
        res = (0,float('inf'))

        for i in range(left,right+1):
            if count[ord(s[i])] > 0:
                cur_count[ord(s[i])] += 1
                if cur_count[ord(s[i])] >= count[ord(s[i])]:
                    cur_freq[ord(s[i])] = True
        if freq == cur_freq:
            return s[left:right+1]

        while right < len(s):
            while right<len(s) and count[ord(s[left])] == 0:
                if left==right:
                    right+=1
                    if right == len(s): break
                    if count[ord(s[right])] > 0:
                        cur_count[ord(s[right])] += 1
                        if cur_count[ord(s[right])] >= count[ord(s[right])]:
                            cur_freq[ord(s[right])] = True
                left+=1
            while freq == cur_freq:
                res = min(
                    res,
                    (left, right),
                    key=lambda x: x[1] - x[0]
                )

                if count[ord(s[left])] > 0:
                    cur_count[ord(s[left])] -= 1

                    if cur_count[ord(s[left])] < count[ord(s[left])]:
                        cur_freq[ord(s[left])] = False

                left += 1

            if right == len(s): break
            right+=1
            if right < len(s):
                if count[ord(s[right])] > 0:
                    cur_count[ord(s[right])] += 1
                    if cur_count[ord(s[right])] >= count[ord(s[right])]:
                        cur_freq[ord(s[right])] = True
            while freq == cur_freq:
                res = min(res, (left,right), key=lambda x:x[1]-x[0])
                
                if count[ord(s[left])] > 0:
                    cur_count[ord(s[left])]-=1
                    if cur_count[ord(s[left])] < count[ord(s[left])]:
                        cur_freq[ord(s[left])] = False
                
                left += 1
        
        if res[1] != float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""
