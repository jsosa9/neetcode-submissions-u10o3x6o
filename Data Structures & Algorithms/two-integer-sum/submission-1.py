class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        so we use a hashmap 
        key is the desired number
        value is the index 
        """
        hm = {}

        for i, num in enumerate(nums):
            desired_value = target - num
            if desired_value in hm:
                return [hm[desired_value], i]
            hm[num] = i