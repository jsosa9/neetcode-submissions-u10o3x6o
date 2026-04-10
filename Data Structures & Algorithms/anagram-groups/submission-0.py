class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        iterate through the strings 
        the key should be the sorted word 
        if the sorted word is a key we add the actual word to the value arr
        otherwise we make the key 

        """
        hm = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in hm:
                hm[sorted_s] = [s]
            else:
                hm[sorted_s].append(s) 
        return list(hm.values())

            
