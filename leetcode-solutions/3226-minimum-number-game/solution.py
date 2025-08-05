class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,3] -> int, even length
        arr = []
        Remove - alice and bob remove the smallest element, in the same order
        Append - Bob appends first followed by alice, until nums is empty

        Time: O(n logn)
        Space: O(1)
        """

        nums.sort()
        arr = []
        a, b = 0, 1

        # for i in range(0, len(nums), 2):
        while a < len(nums) and b < len(nums):
            arr.append(nums[b])
            arr.append(nums[a])
            a += 2
            b += 2
        
        return arr
