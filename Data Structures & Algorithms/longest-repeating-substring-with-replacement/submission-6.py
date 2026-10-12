class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        hm = {}
        top_c = 0
        top = 0
        while r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            top_c = max(hm.values())
            while (r - l + 1) - top_c > k:
                hm[s[l]] -= 1
                l+=1    
            else:
                r+=1
            top = max(top, r - l)
        return top