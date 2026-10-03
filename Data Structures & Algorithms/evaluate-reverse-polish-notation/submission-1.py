class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def math(op1,op2,operator):
            if operator == '/':
                return int(op2/op1)
            elif operator == '*':
                return op1*op2
            elif operator == '+':
                return op1+op2
            else:
                return op2-op1

        for tok in tokens:
            if tok not in {'+','-','/','*'}:
                stack.append(int(tok))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(math(op1,op2,tok))
        
        return stack[-1]