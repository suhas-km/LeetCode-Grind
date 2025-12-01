class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        # last occurrence index for each value
        last_idx = {}
        for i, v in enumerate(nums):
            last_idx[v] = i

        ans = 0
        for v in nums:
            greater_count = n - 1 - last_idx[v]   # all positions after the last v
            if greater_count >= k:
                ans += 1

        return ans



# class Solution:
#     def countElements(self, nums: List[int], k: int) -> int:
#         # 1. Frequency map
#         freq = {}
#         for num in nums:
#             freq[num] = freq.get(num, 0) + 1

#         # 2. Find global range
#         mn = min(freq.keys())
#         mx = max(freq.keys())

#         # 3. Build suffix count of how many elements are greater than each value
#         greater = {}
#         running = 0

#         # Iterate from max → min
#         for val in range(mx, mn - 1, -1):
#             if val in freq:
#                 greater[val] = running   # how many elements strictly > val
#                 running += freq[val]

#         # 4. Count qualified elements
#         ans = 0
#         for num in nums:
#             if greater[num] >= k:
#                 ans += 1

#         return ans

