# from typing import List

# class Solution:
#     def maximumSum(self, nums: List[int]) -> int:
#         def sum_digits(n: int) -> int:
#             s = 0
#             while n:
#                 s += n % 10
#                 n //= 10
#             return s

#         max_val = -1
#         groups = {}  # Maps each digit sum to the largest number with that digit sum
        
#         for num in nums:
#             digit_sum = sum_digits(num)
#             if digit_sum in groups:
#                 # Check candidate sum with the current number and the best seen so far
#                 max_val = max(max_val, groups[digit_sum] + num)
#                 # Update the group with the larger number
#                 groups[digit_sum] = max(groups[digit_sum], num)
#             else:
#                 groups[digit_sum] = num
        
#         return max_val

from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(n: int) -> int:
            total = 0
            while n:
                total += n % 10
                n //= 10
            return total

        groups = {}
        # Group numbers by their digit sum.
        for num in nums:
            ds = sum_digits(num)
            groups.setdefault(ds, []).append(num)

        max_sum = -1
        # For each group with at least two numbers, calculate the candidate sum.
        for ds, group in groups.items():
            if len(group) >= 2:
                group.sort(reverse=True)  # sort to get the two largest numbers easily
                candidate = group[0] + group[1]
                max_sum = max(max_sum, candidate)
        return max_sum


