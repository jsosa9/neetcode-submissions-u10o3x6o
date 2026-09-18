class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_1 = {}
        hm_2 = {}
        for l in s:
            hm_1[l] = hm_1.get(l, 0) + 1 
        for l in t:
            hm_2[l] = hm_2.get(l, 0) + 1 

        if hm_1 == hm_2:
            return True 
        else:
            return False
        