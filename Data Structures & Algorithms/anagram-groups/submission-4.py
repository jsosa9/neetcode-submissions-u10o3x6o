class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        so the key is the hashset version of the word in 
        alphabetical order and then the value is going to
        be the list of words that has those same letters

        and in the end we just return all of the values

        1 : sort the current word 
        if the current word does not exist in the hm then we add 
        - the alphabetical sorted version as the key 
        - value is the word itself 

        """
        finalHm = {}

        for w in strs:
            # assuming this is right (i looked it up just for the syntax)
            sorted_w = "".join(sorted(w))
            if sorted_w not in finalHm:
                finalHm[sorted_w] = [w]
            else:
                # had to look up this syntax i always fotget how simple it is compared to java with the whole <ArrayList> thing
                finalHm[sorted_w].append(w)
            # now we want to return a list of the hashmap values so a list within a list
        return list(finalHm.values())
        
                
            


