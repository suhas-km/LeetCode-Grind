from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for val, freq in countMap.items():
            buckets[freq].append(val)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
        # time: O(n), even though k could be the sizes individual lists inside the bucket, its max value can still only be n(input size)
        # space: O(n)
