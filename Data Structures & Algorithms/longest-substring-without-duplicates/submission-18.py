class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        find the longest seq of non repeating char `
        """
        l, r = 0, 0
        t = set()
        top = 0
        if len(s) == 1:
            return 1
        while r < len(s):
            if s[r] in t:
                t.remove(s[l])
                l+=1
            else:
                t.add(s[r])
                r+=1
            top = max(len(t), top)
        return top
