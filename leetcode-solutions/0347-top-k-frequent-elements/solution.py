class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for value, freq in countMap.items():
            buckets[freq].append(value)
        
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                res.append(n)

                if len(res) == k:
                    return res
                    
