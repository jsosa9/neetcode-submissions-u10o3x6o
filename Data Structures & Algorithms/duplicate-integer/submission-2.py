class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        this is the classic hashset problem 
        we make a set and then if the number isn't already in the set we add it 
        if it is in the set we return false 
        once done with the set then we return true 
        """
        hs = set([])
        for n in nums:
            if n not in hs:
                hs.add(n)
            else: 
                return True
        return False
