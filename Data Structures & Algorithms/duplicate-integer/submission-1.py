class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        so basically i need a hashset to track duplicates 

        i iterate through the array 
        before adding the element if the element is already in the set 
            we return true 
        otherwise we return the element and continue 
        outside the loop we return false 
        """
        hs = set([]) 
        for num in nums:
            if num in hs:
                return True
            else:
                hs.add(num)
        return False
        