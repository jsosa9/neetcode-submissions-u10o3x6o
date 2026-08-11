class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        * so we have pointers at start and end for specific condtion 
        * for things that we need multiple of the smae condition like there is more 
        then
        
        so we need 3 pointers why dont we have one at the start one at the end and then the 
        third one is the left + 1 
        """
        nums = sorted(nums)
        l = []
        for i in range(len(nums)):
            left = i + 1 
            right = len(nums) - 1
            while left < right:
                k = nums[i] + nums[left] + nums[right]
                if k == 0:
                    if [nums[i], nums[left], nums[right]] not in l:
                        l.append([nums[i], nums[left], nums[right]])
                    left+=1
                elif k > 0:
                    right -= 1
                else:
                    left +=1
        return l 

        