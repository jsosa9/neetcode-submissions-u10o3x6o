class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        since it has to be changed in place we cannot just simply make this a 
        set so we have to make a way to make it have unique elements while 
        not making a whole new array 

        we can iterate throuhg it add each item to a set then continue 
        and if the current is in the set then we remove it form the list 
        """
        i, j = 1, 1

        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i 