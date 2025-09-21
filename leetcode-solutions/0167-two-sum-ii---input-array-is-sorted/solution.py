class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            
            if target > total:
                l += 1
            
            elif target < total:
                r -= 1

            else:
                return [l+1, r+1]
         # So if you find a match at l = 0, r = 2, that means the solution involves the 1st and 3rd numbers in the list.
