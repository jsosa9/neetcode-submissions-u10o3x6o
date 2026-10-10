class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        """
        nums = sorted(nums)
        print(nums)
        z = []
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1
            while l < r: 
                x = nums[l] + nums[i] + nums[r]
                if x == 0:
                    if [nums[l], nums[i], nums[r]] not in z:
                        z.append([nums[l], nums[i], nums[r]])
                    r-=1
                    l+=1
                elif x > 0:
                    r-=1
                else:
                    l+=1
        return z 

                    