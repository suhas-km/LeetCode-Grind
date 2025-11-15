class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        INT_MIN = -2**31
        INT_MAX = 2**31 -1

        i = 0
        res = 0

        if not s:
            return 0
        
        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        
        elif s[i] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        if res * sign <= INT_MIN:
            return INT_MIN

        elif res * sign >= INT_MAX:
            return INT_MAX

        else:
            return res * sign
