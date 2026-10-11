class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        """
        if len(s) == 1:
            return 1
        l = 0
        r = 0
        w = set()
        top = 0
        while r < len(s):
            if s[r] not in w:
                w.add(s[r])
                r+=1
            else:
                while s[r] in w:
                    w.remove(s[l])
                    l+=1
            top = max(top, r-l)
        return top
