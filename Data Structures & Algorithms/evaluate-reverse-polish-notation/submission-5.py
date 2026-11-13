class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # go through the tokens
        # if it's an operator pop the top 2 operands and evaluate and put the result on the stack
        # if it is an operand put it on the stack
        # if only one operand is left at the end return it

        stack = []
        operators = ['+' , '-', '*', '/']

        for t in tokens:
            if t in operators:
                right = stack.pop()
                left  = stack.pop()
                
                if t == '+':
                    res = left + right
                elif t == '-':
                    res = left - right
                elif t == '*':
                    res = left * right
                else:
                    res = int(float(left) / right)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack[-1]                         