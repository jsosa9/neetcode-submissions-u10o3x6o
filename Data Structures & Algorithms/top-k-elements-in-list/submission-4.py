class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        would need a hashmap 
        - key is the value 
        - value is the count of tiems it appears 

        then we make a heap size k and then iterate through the hashmap based on the values
        with that we return those corresponding keys 
        """          
        # hm portion
        hm = {}    
        for v in nums:
            hm[v] = hm.get(v, 0) + 1
        heap = []
        for v, count in hm.items():
            heapq.heappush(heap, (count, v))
            if len(heap) > k:
                heapq.heappop(heap)
        return [v for count, v in heap]