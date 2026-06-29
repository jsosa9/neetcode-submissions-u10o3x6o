class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        x === y break stones 
        x < y x is destroyed 
        and y's new weight is y - x 

        now re reading since w eneed 2 heaviest stones each stpe and 
        i assuem there is no sort we use a heap which now makes senes 
        """
        negate_heap = [-x for x in stones]
        heapq.heapify(negate_heap)
        while len(negate_heap) > 1:
            s1 = -1 * heapq.heappop(negate_heap)
            s2 = -1 * heapq.heappop(negate_heap)
            print(s1)
            print(s2)
            if s1 < s2:
                s2 = s2 - s1
                s2 = s2 * -1
                heapq.heappush(negate_heap, s2)      
            elif s1 > s2:
                s1 = s1 - s2
                s1 = s1 * -1
                heapq.heappush(negate_heap, s1)      
            else:
                s1, s2 = 0, 0
            print(negate_heap)
            if len(negate_heap) == 0: 
                return 0
        return -1 * heapq.heappop(negate_heap)

