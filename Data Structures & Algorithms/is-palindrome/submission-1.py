class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        2 ptr approach 
        so i have to make a left and right poitner
        the left is at 0 
        right is at the length or last letter 

        remove all spaces in the string and just make it 
        all lowercase for safety and ease 

        then we have to compare the left and right 
            if there the same we continue 
            if there not we have to return false 
        """

        clean_s = "".join(char.lower() for char in s).replace(" ", "")
        left = 0
        right = len(clean_s) - 1

        while left < right:
            print(clean_s)
            while left < right and not clean_s[left].isalnum():
                left += 1
            while left < right and not clean_s[right].isalnum():
                right -=1
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
        return True

        