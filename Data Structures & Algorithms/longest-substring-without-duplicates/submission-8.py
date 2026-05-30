class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l, r = 0, 0
        top = 0 
        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l+=1
            hs.add(s[r])
            r+=1
            top = max(top, len(hs))
        return top 