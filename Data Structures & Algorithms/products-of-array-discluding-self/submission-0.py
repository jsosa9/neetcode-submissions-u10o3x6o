class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
       so we want a suffix and prefix 
       we take the elements before the current element 
       put that in an array then multiply all of it to 
       get the sum 

       then we do the same for the elements that come after 
       the current element we're iterating through 
       """ 

        left = [] 
        running = 1
        for i in range(len(nums)):
            left.append(running)
            running = running * nums[i]
        right = []
        # begin at -1 
        # go all the way back down to index -1 without skipping
        # go backwards by 1 each time (-1 means go backwards)
        running = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(running)
            running = running * nums[i]
            #need to reverse since its right to left 
        #only need one loop since both have the same number of elements
        rev_right = right[::-1]
        print(left)
        print(rev_right)
        outputArr = []
        for i in range(len(left)):
            outputArr.append(left[i] * rev_right[i])
        return outputArr

