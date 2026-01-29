class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)

        for i in range(n):
            res[i] = nums[i]
            res[i + n] = nums[i]
        
        return res
        
        # # loop nums twice and keep appending vals to res
        # res = []

        # for i in range(len(nums)):
        #     res.append(nums[i])

        # for j in range(len(nums)):
        #     res.append(nums[j])

        # return res
    
    # time: O(2 * N) -> O(N)
    # space: O(2 * N) -> O(N)
