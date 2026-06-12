class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x, y in points:
            # whatever formula i forgot 
            heapq.heappush(heap, ((x**2 + y**2)**0.5, x, y))
        
        finHeap = []
        while k > 0:
            # dist = heapq.heappop(heap)
            # x = heapq.heappop(heap)
            # y = heapq.heappop(heap)
            dist, x, y = heapq.heappop(heap)
            finHeap.append([x, y])
            k-=1
        return finHeap