class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        res = []

        hm2 = defaultdict(list)
        for i, val in hm.items():
            hm2[val].append(i)
        
        for i in range(len(nums), -1, -1):
            if i in hm2:
                for element in hm2[i]:
                    res.append(element)
                    if len(res) == k:
                        return res

        return res

