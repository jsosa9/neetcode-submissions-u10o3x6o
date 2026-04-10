class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        return all pairs of 3 who 
        have 3 indexes values sum to 0 
        and all 3 indexes are distinct 
        """
        
        arr = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right: 
                if val + nums[left] + nums[right] == 0:
                    arr.append([val, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right-=1
                else:
                    left+=1
                    # left+=1
        return arr
                


