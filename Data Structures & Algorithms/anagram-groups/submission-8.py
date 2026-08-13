class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        so the words have to be the same in the sense that the letters 
        are the same 

        """
        hm = {}
        for w in strs: 
            order = "".join(sorted(w))
            hm.setdefault(order, []).append(w)
        return list(hm.values())
        