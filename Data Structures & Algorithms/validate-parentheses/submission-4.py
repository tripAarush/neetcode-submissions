class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {']':'[', '}':'{', ')':'('}
        for sign in s:
            if sign in {']', '}', ')'}:
                if not stack or stack[-1]!=hashmap[sign]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(sign)

        return True if not stack else False