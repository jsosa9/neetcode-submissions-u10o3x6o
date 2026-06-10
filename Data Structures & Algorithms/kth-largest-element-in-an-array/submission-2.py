# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # so the heap has to be of size k 
#         # and this would mean we return negated_heap[k]
#         heap = []
#         for n in nums:
#             if len(heap) < k:
#                 heapq.heappush(heap, n)
#             if len(heap) > k:
#                 heapq.heappop()
#         print(heap)
#         return 1

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            else:
                if heap[0] < n:
                    heapq.heappushpop(heap, n)
                else: 
                    continue
        return heap[0]


        