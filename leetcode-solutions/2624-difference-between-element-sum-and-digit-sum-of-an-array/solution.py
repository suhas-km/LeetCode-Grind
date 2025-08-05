class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        """
        Time: o(n * m), m is the size of the number
        Space: o(1)
        """

        elementSum = sum(nums)
        digitSum = 0

        for number in nums:
            while number > 0:
                digit = number % 10
                digitSum += digit
                number = number // 10
        
        return abs(digitSum - elementSum)
