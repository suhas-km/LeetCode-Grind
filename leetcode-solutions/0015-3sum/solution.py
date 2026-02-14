class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            # if i > 0 and nums[i] == nums[i - 1]:
            #     continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[r] + nums[l]
                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                
                elif total < 0:
                    l += 1
                
                else:
                    r -= 1
        
        return [list(x) for x in res]

