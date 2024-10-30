class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            # apply when it is sorted
            mid =  (i + j)//2     # // is for integer division - round of for floor value

            if target == nums[mid]:
                return mid

            elif target < nums[mid]:
                j = mid-1
                
            else:
                i = mid+1
                
                 
        return -1
