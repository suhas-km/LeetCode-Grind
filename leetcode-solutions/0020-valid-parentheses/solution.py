class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            
            elif i == ')' or i == '}' or i == ']':
                if stack:
                    val = stack.pop()
                    if (i == ')' and val != '(') or (i == '}' and val != '{') or (i == ']' and val != '['):
                        return False

                else:
                    return False
        
        return len(stack) == 0

