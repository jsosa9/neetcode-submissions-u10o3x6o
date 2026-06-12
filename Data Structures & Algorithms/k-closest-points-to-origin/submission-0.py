class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, ((x**2 + y**2)**0.5, x, y))

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        return res
