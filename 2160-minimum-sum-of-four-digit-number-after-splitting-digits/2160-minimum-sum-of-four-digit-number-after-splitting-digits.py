class Solution:
    def minimumSum(self, num: int) -> int:
        string=str(num)
        s=sorted(string)
        m=s[0]+s[2]
        n=s[1]+s[3]
        return (int(m)+int(n))