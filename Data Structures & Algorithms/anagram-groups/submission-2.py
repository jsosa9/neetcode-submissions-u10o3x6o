class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        an anagram is a word that reads the same way foward and backwards

        I use a hashmap for each word 
        for each word i make a key of the word in alphabetical order 
        then the value for that is the list of words that fit under it  
        """
        hm = {}
        output = []
        for s in strs:
            print(s) 
            sorted_s = "".join(sorted(s))
            if sorted_s not in hm:
                hm[sorted_s] = [s]
            else: 
                hm[sorted_s].append(s)
        return list(hm.values())


