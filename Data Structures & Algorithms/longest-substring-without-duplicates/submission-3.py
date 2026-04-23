class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
    seems to be a sliding window and then i can use a hashset if the letter is in the set 
    that is the current max thne the l = r and then r += 1 
        """
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
        