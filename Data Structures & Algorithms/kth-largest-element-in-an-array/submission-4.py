class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        so kth largest menas we would have to use a heap because 
        when we pop from the heap we pop the smallest one anyways so its 
        the easiest appraoch especially since we cant sort 

        we make a heap 
        add items to the heap until the size is > k
        if so we pop or maybe we can peek and then compare that with the current value 

        if the curr is greater then we remove the peek and put that in 
        otherwise continue 

        in the end we pop and return that 
        """
        heap = []
        heapq.heapify(heap)
        for x in nums:
            if len(heap) < k: 
                heapq.heappush(heap, x)
            else:
                peek = heapq.heappop(heap)
                if x > peek:
                    heapq.heappush(heap, x)
                else:
                    heapq.heappush(heap, peek)
        return heapq.heappop(heap)

            
     