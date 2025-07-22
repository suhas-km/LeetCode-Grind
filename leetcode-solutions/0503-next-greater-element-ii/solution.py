class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        n = len(nums)
        stack = []

        for i in range(0, 2*n):
            index = i % n-1
            
            while stack and nums[index] > stack[-1][1]:
                idx, value = stack.pop()
                res[idx] = nums[index]

            stack.append([index, nums[index]])
        
        return res
