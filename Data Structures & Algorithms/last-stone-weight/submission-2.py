class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # negate the arr into a obj
        negate_heap = [-x for x in stones]
        # get the negated arr into the heap encoding 
        heapq.heapify(negate_heap)
        # once the length is greater then 1 you can have the stones battle 
        while len(negate_heap) > 1: 
            # popping it always takes the largest
            first_lg = heapq.heappop(negate_heap)
            second_lg = heapq.heappop(negate_heap)
            # raising the conditoins the problem bought up
            if first_lg != second_lg:
                new_el = first_lg - second_lg
                heapq.heappush(negate_heap, new_el)
                # returning the highest item in the negated heap original value
                # otherwise we return 0 
        return -negate_heap[0] if negate_heap else 0