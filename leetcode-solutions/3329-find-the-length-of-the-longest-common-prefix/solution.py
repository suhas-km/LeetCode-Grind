class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # pick the smaller len
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set: # while non-zero
                prefix_set.add(n)
                n = n // 10
        
        res = 0
        for n in arr2:
            while n and n not in prefix_set: # while n is non-zero and n not in prefixSet
                n = n //10
            if n != 0:
                res = max(res, len(str(n)))
        
        return res

        # time: O((n.log) * (m.log))
