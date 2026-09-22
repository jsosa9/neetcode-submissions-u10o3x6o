class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split()).lower()
        l = 0
        r = len(s) - 1
        if len(s) == 1:
            return True
        while l < r:
            if s[l].isalnum() is False:
                l+=1
            elif s[r].isalnum() is False:
                r-=1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r-=1
        return True