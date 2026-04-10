class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hm = {}

        # adding everything into the hashmap to track value and freq
        for n in nums: 
            if n not in hm:
                hm[n] = 1
            else: 
                hm[n] += 1
        

        for key, freq in hm.items():
            # if the size of the heap is less then k we add 
            if len(heap) < k:
                heapq.heappush(heap, (freq, key))
            # if the size of the heap is greater then or equal to k
            # we have to check the smallest elemnt of the heap 
            elif freq > heap[0][0]:
                heapq.heappushpop(heap, (freq, key))
            continue
        return [pair[1] for pair in heap]
