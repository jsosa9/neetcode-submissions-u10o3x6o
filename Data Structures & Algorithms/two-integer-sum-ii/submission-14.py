class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        so what 2 numbers add up to the target 
        """
        hm = {}
        for i, n in enumerate(numbers):
            # key is going to be the value needed so target - current 
            # value will be the index 
            c = target - n
            if n not in hm: 
                hm[c] = hm.get(c, i)
            else:
                return [hm[n] + 1, i + 1]