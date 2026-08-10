class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        s = deeedbbcccbdaa k = 3 
        ddbbcccbdaa
        ddbbbdaa
        dddaa
        aa

        we have the return string that holds the current verison of the word 

        for each character in the current version of the word 
        we need to basically add it to a hashmap and then get the count ofr it 

        """
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        return "".join(c * count for c, count in stack)