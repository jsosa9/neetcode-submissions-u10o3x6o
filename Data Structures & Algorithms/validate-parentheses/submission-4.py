class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        print(len(stack))
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")" or c == "]" or c == "}":
                if c == ')':
                    if len(stack) > 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                    
                if c == ']':
                    if len(stack) > 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False

                if c == '}':
                    if len(stack) > 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True 
        else:
            return False