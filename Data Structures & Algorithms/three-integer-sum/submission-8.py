class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = []
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1

            while l < r:
                # to large dec right, to small inc left 
                if nums[l] + nums[r] + nums[i] == 0:
                    if [nums[l], nums[r], nums[i]] not in x:
                        x.append([nums[l], nums[r], nums[i]])
                    r-=1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1    
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1    
        print(x)
        return x