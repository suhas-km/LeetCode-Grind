class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # APPROACH 1
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate

        # APPROACH 2
        # The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), it will always occupy the middle position when the array is sorted.
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]
