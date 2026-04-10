class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        we need a heap with 2 stones or elements and then 
        preform the math based on the elements 

        first we get the 2 largest elements 
        and then once done we do the operations on the elements 
        """

        negate_heap = [-x for x in stones]
        heapq.heapify(negate_heap)
        while len(negate_heap) > 1:
            # pull the 2 largest elements 
            first_lg = heapq.heappop(negate_heap)
            second_lg = heapq.heappop(negate_heap)
            if first_lg != second_lg:
                # still negated
                new_el = first_lg - second_lg
                heapq.heappush(negate_heap, new_el)
        return -negate_heap[0] if negate_heap else 0
        """
        now that stones is a heap 
        we need to get teh 2 largest digits 
        """

        """
        heap = []
        for s in stones:
            if len(heap) < 2:
                heapq.heappush(heap, s)
            elif s > heap[0]:
                heapq.heappushpop(heap, s)
        
        if heap[1] > heap[0]:
            return heap[1] - heap[0]
        else:
            return 0
        """
        
        