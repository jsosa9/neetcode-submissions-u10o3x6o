class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1 : so the window is fixed to k because we have k replacements 
        2 : and then to track count we can have a hashmap where we track the count of each 
        letter
        3 : we only take the value of the first letter and then ignore that we then have to 
        get the value of the rest of the letters if that sum of there values is more then 
        k then we have to cut off the sequence 

        4 : we keep doing this and then when we reset we have to pop one from the left pointer 
        and then pop that same letter -=1 in the hm as well until right - left + 1 = k          
        """
        hm = {}
        l, r = 0, 0
        top_score = 0
        for c in s: 
            """
            states 
            - expanding the hm to look for more 
            - reached full capicity k and have to cut down 
            """
            # hm.values() - top_c > k
            hm[c] = hm.get(c, 0) + 1    
            top_c = max(hm.values())
            while (r - l + 1) - top_c > k: 
                hm[s[l]] -= 1
                l+=1 
            else: 
                top_score = max(top_score, r - l + 1) 
                r+=1
        return top_score

