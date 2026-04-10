class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        parse through the input for each word 
        we get the alphabetical version of this word 
        if it already exists as a key in the hashmap we add to the value 
        - add the original word into the value 
        - otherwise we add the key value pair 
        """
        
        hm = {}
        for w in strs:
            w_sorted = "".join(sorted(w))
            if w_sorted not in hm:
                hm[w_sorted] = [w]
            else: 
                hm[w_sorted].append(w)


        return list(hm.values())