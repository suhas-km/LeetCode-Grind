class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter and reverse the hm's key:value -> key(value):value(key)
        
        eleToFreq = Counter(nums)
        res = []
        freqToEle = defaultdict(list)

        for key, val in eleToFreq.items():
            freqToEle[val].append(key)
        
        maxFreq = max(freqToEle.keys())
        minFreq = min(freqToEle.keys())

        for freq in range(maxFreq, minFreq - 1, -1):
            if freq in freqToEle:
                for ele in freqToEle[freq]:
                    if len(res) < k:
                        res.append(ele)
            if len(res) == k:
                break

        return res

