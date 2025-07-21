class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums2)

        for i, v in enumerate(nums2): # creating monotonous stack for reference
            while stack and v > stack[-1][1]:
                stackInd, stackValue = stack.pop()
                res[stackInd] = v

            stack.append([i, v])
        
        res2 = []
        for i in nums1:
            res2.append(res[nums2.index(i)])
    
        return res2
