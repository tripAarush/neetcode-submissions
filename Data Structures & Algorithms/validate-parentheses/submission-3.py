class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}

        i=0
        for i in range(len(s)):
            if s[i] in hashmap:
                if len(stack) == 0 or hashmap[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
                    continue
            stack.append(s[i])
        
        return not stack