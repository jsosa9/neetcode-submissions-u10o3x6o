class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for w in strs:
            sort = "".join(sorted(w))
            hm[sort] = hm.get(sort, [])
            hm[sort].append(w)
        return list(hm.values())

