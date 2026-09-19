class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            if n not in hm:
                t = target - n
                hm[t] = hm.get(t, i)
            else:
                return [hm[n],i]
        return [0,0]