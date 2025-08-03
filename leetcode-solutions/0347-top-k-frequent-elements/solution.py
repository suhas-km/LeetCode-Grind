class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        maxHeap = []
        res = []

        count = Counter(nums)

        for i, v in count.items():
            maxHeap.append([-v, i])
        
        heapq.heapify(maxHeap)

        while k > 0:
            op = heapq.heappop(maxHeap)
            res.append(op[1])
            k -= 1

        return res
