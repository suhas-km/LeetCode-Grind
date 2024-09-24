class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        deduplicate = set()  # Using a set to avoid duplicates
        
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1  # Two pointers for each 'i'
            while start < end:
                current_sum = nums[i] + nums[start] + nums[end]
                if current_sum == 0:
                    # If we found a triplet, add it to the set to avoid duplicates
                    deduplicate.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif current_sum < 0:
                    # If sum is less than zero, move the start pointer to increase sum
                    start += 1
                else:
                    # If sum is greater than zero, move the end pointer to decrease sum
                    end -= 1
        
        # Convert the set of triplets into a list of lists and return
        return [list(triplet) for triplet in deduplicate]