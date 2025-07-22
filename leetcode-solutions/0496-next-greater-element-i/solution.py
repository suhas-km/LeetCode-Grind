class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = [-1] * len(nums2)
        stack = []

        for i, v in enumerate(nums2):
            while stack and v > stack[-1][1]:
                stackIndex, stackVal = stack.pop()
                res[stackIndex] = v
            stack.append([i, v])
        
        res2 = []
        for i in nums1:
            res2.append(res[nums2.index(i)])

        return res2
