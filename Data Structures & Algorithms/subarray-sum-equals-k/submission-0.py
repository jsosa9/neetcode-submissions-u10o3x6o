class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        total amount of subarrays that equal k 

        since there are + and - numbers we cant use pointers 

        thinking of having a running count alongside a hashmap 
        and every time the count == k we inc the subarray found 
        conut by 1 

        the hahsmap would have 
        key : count needed 
        value : times it has appeared 
        """
        count = 0 
        re = 0 
        hm = {0 : 1}
        for n in nums: 
            count += n 
            c = count - k 
            if c in hm:
                re += hm[c]
            hm[count] = hm.get(count, 0) + 1 
        return re 