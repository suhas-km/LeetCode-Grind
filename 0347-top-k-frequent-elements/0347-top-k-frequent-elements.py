class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to count the frequency of each element in nums
        count = {}

        # Initialize 'freq', a list of empty lists, to categorize numbers by their frequency.
        # The length of 'freq' is len(nums) + 1 to accommodate: - Each unique frequency count from 0 to the maximum possible count (i.e., all elements are the same).
        # This ensures all possible scenarios, including the edge case where all elements in 'nums' have the same value, are handled.
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums: # Loop to get counts/frequency of each number in "nums"
            # Increase the count for each number 'n' in the dictionary 'count', using get() to return 0 if 'n' is not yet in the dictionary
            count[n] = 1 + count.get(n, 0)

        # Place each number in the 'freq' list according to its frequency
        for n, c in count.items(): # starting loop on every key : value pair
            # Append the number 'n' to the sublist in 'freq' at index 'c', where 'c' is the frequency of 'n'
            freq[c].append(n) # this number 'n' appears exactly 'c' number of times

        # initialized Result list to store the top k frequent elements
        res = []

        # Iterate through the 'freq' list from the highest possible frequency to the lowest
        for i in range(len(freq) - 1, 0, -1):  # Start from the end of 'freq' to ensure we get the most frequent elements first
            # Check numbers with frequency 'i'
            for n in freq[i]:
                # Add number 'n' to the result list 'res'
                res.append(n)
                # Once we have added k elements to the result, return it immediately to end the function
                if len(res) == k:
                    return res

