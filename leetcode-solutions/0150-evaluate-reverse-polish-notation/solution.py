from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
                
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    result = num2 + num1
                elif token == '-':
                    result = num2 - num1
                elif token == '*':
                    result = num2 * num1
                else:  # token == '/'
                    # Use int() to truncate toward zero (required by problem)
                    
                    result = int(num2 / num1)
                stack.append(result)
        
        return stack[0]
