class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int("".join(map(str, digits)))
        result += 1 
        ans = []
        result = str(result)
        for c in result:
            ans.append(c)
        return ans