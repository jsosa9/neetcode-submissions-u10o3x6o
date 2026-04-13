class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        since we have to find the longest we go with sliding window 
        to keep track of each letter we then use hashmap 

        we then get the highest freq letter and if the highest count - k 
        """
        l, r = 0, 0
        hm = {}
        # max freq letter count 
        # max streak 
        streak = 0
        freq = 0
        while l <= r and r < len(s):
            hm[s[r]] = hm.get(s[r], 0) + 1
            freq = max(hm[s[r]], freq)
            while r - l + 1 - freq > k:
                hm[s[l]] = hm.get(s[l], 0) - 1
                l+=1 
            streak = max(r - l + 1, streak)
            r+=1 
        return streak

