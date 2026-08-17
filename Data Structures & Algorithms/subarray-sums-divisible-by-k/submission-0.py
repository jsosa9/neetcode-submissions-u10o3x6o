class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        running count for each element and also return 

        key : count 
        value : index 
        """ 
        hm = {0 : 1}
        count = 0 
        g_count = 0
        for i,n in enumerate(nums):
            count += n 
            rem = count % k
            if rem in hm:
                g_count += hm[rem]
            hm[rem] = hm.get(rem, 0) + 1 
        return g_count