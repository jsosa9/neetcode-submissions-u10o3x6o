class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        so we have to get each word and sort it in alphbetical order 
        once sorted that is the key value in the hashamp if it doesnt exist alreayd
        if it does exist we find the key and append the original word as the value 
        then in the end we return the list of values 
        """   
        hm = {}
        for w in strs:
            sorted_w = "".join(sorted(w))
            print(sorted_w)
            if sorted_w in hm: 
                hm[sorted_w].append(w)
            else:
                hm[sorted_w] = [w]
        print(list(hm.values()))
        return list(hm.values())
