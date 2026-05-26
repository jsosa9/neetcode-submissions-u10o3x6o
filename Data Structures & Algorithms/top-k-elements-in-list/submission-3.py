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
        return heapq.nlargest(k, hm, key=lambda x: hm[x])