class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        well we can use a hahsmap where 
        the key is the original value fro mthe array 
        the value of the hm is the index its ucrrently at 

        before we add we check the current keys in the hm to see if we find a pair

        """
        hm = {}

        for i, n in enumerate(nums):
            """
            Take the current value we're passing through and add it with every key in 
            the hashmap 

            if the total is equal to target reutnr both indicides else add the current      
            value to the hm 
            """
            if len(hm) > 0:
                # comapre the value with every value in the hm 
                for k in hm:
                    if n + k == target:
                        return [hm[k], i]
            hm[n] = i
        