class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count the frequency of each element in nums
        count = {}

        # Create a list of empty lists to store numbers with the same frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the frequency of each number in nums
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Place each number in the 'freq' list according to its frequency
        for n, c in count.items():
            freq[c].append(n)
        
        # Result list to store the top k frequent elements
        res = []
        
        # Iterate through the 'freq' list from the highest possible frequency to the lowest
        for i in range(len(freq) - 1, 0, -1):
            # Check numbers with frequency i
            for n in freq[i]:
                res.append(n)
                # Once we have added k elements to the result, return it
                if len(res) == k:
                    return res
