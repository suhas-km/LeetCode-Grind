class Solution:
    def isValid(self, s: str) -> bool:
        lookUp = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in lookUp:  # opening
                stack.append(ch)
                
            else:  # closing
                if len(stack) == 0:
                    return False

                open_br = stack.pop()
                if lookUp[open_br] != ch:
                    return False

        return len(stack) == 0

