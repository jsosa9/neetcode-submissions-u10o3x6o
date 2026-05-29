class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        so we need to find all combinations that has 3 numbers that sum up to 0

        this uses a for loop + 2 pointers 
        """
        nums.sort()
        print(nums)
        pair_arr = []
        """
        so we sort the array to iterate it easier 
        for loops is the first element 
        left is the eleemnt after the for element 
        right is the last element in the array

        if too small we do left+=1 
        if too large right-=1 
        """
        for i in range(len(nums) - 1):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if [nums[i],nums[l],nums[r]] in pair_arr:
                        l+=1
                        r-=1
                    else:
                        pair_arr.append([nums[i],nums[l],nums[r]])
                        l+=1 
                        r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        return pair_arr


