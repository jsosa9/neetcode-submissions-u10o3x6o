class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for n in nums:
            if n not in c:
                c.add(n)
            else:
                return True
        print(c)
        return False