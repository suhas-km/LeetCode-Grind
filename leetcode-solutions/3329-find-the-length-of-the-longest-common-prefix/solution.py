class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2): # pick the smaller list
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        for n in arr1:
            while n and n not in prefix_set: # non-zero and not in set
                prefix_set.add(n)
                n = n // 10
        
        res = 0 
        for num in arr2:
            while num and num not in prefix_set: # non-zero and not in set
                print(num)
                num = num // 10
            
            if num != 0:
                res = max(res, len(str(num)))
        
        return res

