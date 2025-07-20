class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # keep track of number of open and close in each call
        # only add open paranthesis if open < n
        # add a closing bracket only if closeed < open
        # return/valid IFF open == closed == 'n'

        stack = [] # hold the paranthesis
        res = [] # list of valid paranthesis combinations

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
