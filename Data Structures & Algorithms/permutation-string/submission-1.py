class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        first we add s1 into a hm 
        then we add s2 into a hm 

        we then check if there equal if so return true 

        if not then we iterate in a for loop froom 
        s1 to s2 

        we add the current letter into the s2 hm 

        we then remove the old letter from the s2 hm which is i - k 

        and then we check if the prev lettr count is 0 if so we delete it from hm 

        we then check if there equal again

        outside of all of this we return false 
        """
        if len(s1) > len(s2):
            return False
            
        s1hm = {}
        for i in s1:
            s1hm[i] = s1hm.get(i, 0) + 1

        s2hm = {}
        for i in range(len(s1)):
            curr = s2[i]
            s2hm[curr] = s2hm.get(curr, 0) + 1

        if s1hm == s2hm:
            return True 

        for i in range(len(s1), len(s2)):
            # add the currnet letter 
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1
            # remove the prev one 
            s2hm[s2[i - len(s1)]] = s2hm.get(s2[i - len(s1)], 0) - 1
            # if prev one is now value is 0 then we remove from hm 
            if s2hm[s2[i - len(s1)]] == 0:
                del s2hm[s2[i - len(s1)]]
            # beefore leaving we check if there equal
            if s1hm == s2hm:
                return True 
        return False
        