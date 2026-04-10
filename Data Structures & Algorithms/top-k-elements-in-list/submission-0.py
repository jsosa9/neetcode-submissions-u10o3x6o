class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        so we want to make a hashmap to keep track 
        of the elements and there frequencies

        then we iterate through the hashmap again and 
        then we return the ones with the value of k 
        """
        hm = {}
        heap = []
        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        for key, val in hm.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]


        