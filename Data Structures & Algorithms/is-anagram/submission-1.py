class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        so we take one word and put it into a hahsmap 
        key is the character value is the counut 
        and then we need to make another hashmap for the 2nd word the hashmap should be the same 

        or instead of comparing them we can iterate the 2nd word and just do -=1 and if we find a word we haven't seen yet in the 
        original hm then we return false 

        leaning towards the 2nd method of comaprison rather then making another hm 
        """ 
        if len(s) != len(t):
            return False

        hm = {}
        for l in s:
            hm[l] = hm.get(l, 0) + 1

        for l in t:
            if l not in hm:
                return False
            hm[l] = hm.get(l, 0) - 1
            if hm[l] < 0:
                return False
        return True


        
        