class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        2 pointers since we only care about the things at the pointers not the values in the middle 
        """
        z = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1 
            while l < r:
                x = nums[i] + nums[l] + nums[r] 
                if x == 0:
                    if [nums[i], nums[l], nums[r]] not in z:
                        z.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                if x > 0:
                    r-=1
                if x < 0:
                    l+=1
        return z
