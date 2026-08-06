class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        the idea is to have sldiidng winow 
        get the longest one 
        add each thing ot a set 
        have a counter that takes the max 
        """
        l, r = 0, 0
        t = set()
        m = 0

        while r < len(s):
            if s[r] in t:
                t.remove(s[l])
                l += 1
            else:
                t.add(s[r])
                r+=1 
            m = max(m, len(t))
        return m
            

        
        
