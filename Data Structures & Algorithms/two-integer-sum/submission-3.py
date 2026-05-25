class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            # we need to check if there is a value in the hm that is equal to the desirevalue
            desiredValue = target - num
            if desiredValue in hm:
                return [hm[desiredValue], i]
            hm[num] = i        
        