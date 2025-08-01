class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        hm2 = {}

        for i in s:
            if i not in hm:
                hm[i] = 1
            hm[i] += 1

        for j in t:
            if j not in hm2:
                hm2[j] = 1
            hm2[j] += 1

        # if hm == hm2:
        #     return True
        return hm == hm2
    
