class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
       solution in O(logn) indicates binary search

       we make the left the start and right the end 
       while left is less then or equal to right 

       we take the whole window divide it in half 
       if the current value is the vallue we want we return the index 
       if the value we want is greater we shift the left pointer and add 1 
       if the value is too small we shif the right pointer and - 1 
        """

        l, r = 0, len(nums) - 1
        while l <= r: 
            mid = (l + r) // 2 

            if nums[mid] == target: 
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        # if we don't get mid in the end it means it failed
        return - 1






