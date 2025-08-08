class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        """

        hm = {}
        
        for i, num in enumerate(nums):
            if not hm:
                hm[num] = i
                continue
            
            complement = target - num
            
            if complement in hm:
                print(hm)
                return [hm[complement], i]
            else:
                hm[num] = i
