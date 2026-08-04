class Solution:
    def isValid(self, s: str) -> bool:
        """
        - so we want to add all of the input into the stack as long as the 
        current char isn't  a closing 
        - if its a closign we peek into the stack and see if the corresponding 
        opening is it 
         - if so continue if not return false 
        """
        stack = []
        # odd cases 
        if len(s) % 2 != 0:
            return False

        for c in s:
            # add to stack 
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                else: 
                    return False
                if x == '(' and c != ')' or x == '[' and c != ']' or x == '{' and c != '}':
                    return False
        if len(stack) >= 1:
            return False
        else:
            return True