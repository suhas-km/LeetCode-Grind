class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        factors = [2, 3, 5]
        visited = set()

        for i in range(n):
            num = heapq.heappop(minHeap)

            if i == n - 1:
                return num
            
            for factor in factors:
                if num * factor not in visited:
                    visited.add(num * factor)
                    heapq.heappush(minHeap, num * factor)

