class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        we can do hashmap and make sure the key is the char and the value
        is the count 

        or we cna just have a hashset where we track if the value is in the hs
        if not we add it if so we continue 
        """
        hm = {}
        x = -1
        for c in s:
            if c not in hm:
                hm[c] = 0
            hm[c] += 1 
        for i,v in enumerate(s):
            if hm[v] == 1:
                x = i
                return x 
        return x