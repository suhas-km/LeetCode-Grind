class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        prefixSet = set()
        for n in arr1: # every values prefix values to be put into set
            while n and n not in prefixSet: # while n is non-zero and not in visited
                prefixSet.add(n)
                n = n // 10
        
        res = 0
        for num in arr2:
            while num and num not in prefixSet: # if this value is invalid aka. not a valid number -> num // 10
                num = num // 10
            
            if num != 0:
                res = max(res, len(str(num)))
        
        return res

