class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        hashmap for frequ

        i was also thinking sorting both in alphabetical order but thats slower i 
        beleive its clsoer to like log(n) or something i know sort isn't optimal 
        """
        hm = {}
        hm_2 = {}

        for l in s:
            hm[l] = hm.get(l, 0) + 1
        
        for l in t:
            hm_2[l] = hm_2.get(l, 0) + 1
        
        if hm == hm_2:
            return True 
        else: 
            return False