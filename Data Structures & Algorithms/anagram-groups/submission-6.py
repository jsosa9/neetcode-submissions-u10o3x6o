class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        so we have to group all of the words that are the exact same alphabetically 

        we can store each word in a hashmap the 
        key : alphabetical version of the word 
        value : the list of words 

        in the end we just return every single value 
        """
        hm = {}

        for word in strs:
            x = "".join(sorted(word))
            hm.setdefault(x, []).append(word)
        print(hm)
        return list(hm.values())