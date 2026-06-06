class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1hm = {}
        for val in s1:
            s1hm[val] = s1hm.get(val, 0) + 1
        s2hm = {}       
        for i in range(len(s1)):
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1
        if s1hm == s2hm:
            return True 
        for i in range(len(s1), len(s2)):
            s2hm[s2[i]] = s2hm.get(s2[i], 0) + 1

            s2hm[s2[i - len(s1)]] = s2hm.get(s2[i - len(s1)], 0) - 1
            if s2hm[s2[i - len(s1)]] == 0:
                del s2hm[s2[i - len(s1)]]
            if s1hm == s2hm:
                return True 
        return False
