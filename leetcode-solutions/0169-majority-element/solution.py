class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Count the occurrences of each number
        count = Counter(nums)

        # Find the element with count > len(nums) // 2
        for num, freq in count.items():
            if freq > len(nums) // 2:
                return num
                
