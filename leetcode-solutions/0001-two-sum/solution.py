class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dictionary storing all the seen values of the list

        for i, value in enumerate(nums): 
            remaining = target - nums[i] #finding the remainnig value to be located in seen {}

            if remaining in seen:
                return [i, seen[remaining]] #if remaining found, Solution reached
            else:
                seen[value] = i # else we append the value to the list
                
