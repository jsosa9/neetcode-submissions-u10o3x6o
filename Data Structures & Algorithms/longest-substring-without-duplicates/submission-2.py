class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        total = 0
        hs = set([])
        print(1)
        while l <= r and r < len(s): 
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            r += 1 
            if len(hs) > total:
                total = len(hs)
        return total
        