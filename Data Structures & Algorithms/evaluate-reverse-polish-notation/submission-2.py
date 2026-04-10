class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        so we definitely use some sort of stack 
        what im thinking is that we store the numbers in the stack
        
        if the len of stack = 2 
            - a + b
        if the len of the stack is 1 
            - current_sum = symbol= current_sum
        
        and then based on the symbol the placement is different 
        """

        stack = []
        current_sum = 0
        for n in tokens:
            if n not in {'+', '*', '-', '/'}:
                stack.append(int(n))
            else:
                if n == '*':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b * a))
                elif n == '+':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b + a))
                elif n == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b - a))
                elif n == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b / a))
        return int(stack.pop())
                # if n == '-' or '/':
                # a + b 
                # a * b

                # b / a
                # b - a
        