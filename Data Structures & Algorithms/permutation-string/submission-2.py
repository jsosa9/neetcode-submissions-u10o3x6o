class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
so to find out if something is a permutation you would have to 
put it in a hashmap and then track the count of each letter 

if the counts match up assuming the size is correctly set then its a permutaiton 
othweise its not and then you shift the window 
        """
        if len(s1) > len(s2):
            return False

        hm_s1 = dict({})
        for val in s1:
            hm_s1[val] = hm_s1.get(val, 0) + 1
        
        hm_s2 = dict({})
        for i in range(len(s1)):
            val = s2[i]
            hm_s2[val] = hm_s2.get(val, 0) + 1

        if hm_s1 == hm_s2:
            return True 

        for i in range(len(s1), len(s2)):
            """
            so the hashmaps are either equal 

            if there not equal then we check if the value is empty 
            if empty we have to remove it if not contineiu but we basically -1 
            """        
            hm_s2[s2[i]] = hm_s2.get(s2[i], 0) + 1
            hm_s2[s2[i - len(s1)]] =  hm_s2.get(s2[i - len(s1)], 0) - 1

            if hm_s2[s2[i - len(s1)]] == 0:
                del hm_s2[s2[i - len(s1)]]
             
            if hm_s1 == hm_s2:
                return True 
        
        
        return False