class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        the length of the shortest string is the length of the longest 
        prefix so we dont go out of bounds 
        """
        
        min_l = 10000000
        for w in strs: 
            if len(w) < min_l:
                min_l = len(w)
        
        """
        for each string now that we know the max length of the prefx 
        we have i = 0 and then we inc as long as we're less then the 
        """
        i = 0 
        while i < min_l: 
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+= 1
        return strs[0][:i]