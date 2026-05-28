class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        so i need to cut out all the spaces and make everything lowercase 
        i need a pointer at 0 and pointer at the end if they match then we shift them
        """    
        new_s = s.replace(" ", "")
        new_s = new_s.lower()
        left, right = 0, len(new_s) - 1 
        print(new_s)
        while left < right:
            if not new_s[left].isalnum():
                left += 1
            elif not new_s[right].isalnum():
                right -= 1
            elif new_s[right] == new_s[left]:
                left+=1
                right-=1
            elif new_s[right] != new_s[left]:
                return False
        return True
            

