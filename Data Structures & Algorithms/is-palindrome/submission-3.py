class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        convert the sentence into lowercase and no spaces 
        while left is < right we checck left and right and if there equal we continue otherwise return false
        in the end we return true 
        """
        conversion = "".join(s.split()).lower()
        left, right = 0, len(conversion) - 1

        while left < right:
            while left < right and not conversion[left].isalnum():
                if left >= len(conversion):
                    return False
                left+=1
            while left < right and not conversion[right].isalnum():
                right-=1
            if conversion[left] == conversion[right]:
                left+=1
                right-=1
            else:
                return False
        return True
        
        