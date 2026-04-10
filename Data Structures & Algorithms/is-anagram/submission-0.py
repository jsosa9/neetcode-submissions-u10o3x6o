class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        so this is a classic hashmap 
        i need to iterate through the first string
            add all of those letters, frequences into the hashmap
        then for the 2nd word i do the same 
            but this time if the letter is in the map 
            i (-1) to the frequency 

            otherwise if its not in the map at all i just return false
        """
        hm = {}

        for l in s:
            hm[l] = hm.get(l, 0) + 1
        
        for l in t:
            if l not in hm:
                return False
            else:
                hm[l] = hm.get(l, 0) - 1

        for key, val in hm.items():
            if val != 0:
                return False
        return True