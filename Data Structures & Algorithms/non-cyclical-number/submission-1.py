class Solution:
    def isHappy(self, n: int) -> bool:
        """
        so a non cynical number is a number when taken you 
        square each individual digit - add them together - solution should be 1 
        outcome = 1 = true 
        outcome != 1 = false 

        why dont i do a 2 pointer or somethine 

        so we need to take each digit square it get the total and then repeat 
        do this over and over again until we get 1 - retunr true 
        if we get a number we've seend befoer as the total return false 
        """

        n = str(n)
        tracker = set()
        l = [0]
        # while l:
        # where im lost is how can i add all of them and keep them 
        w = True 
        while w:
            total = sum(int(d) ** 2 for d in str(n))
            print(tracker)
            if total == 1:
                w = False
                return True
            if total not in tracker:
                tracker.add(total)
            elif total in tracker:
                w = False 
                return False
            n = total
            

        # for digit in n:
        #     digit = int(digit)
        #     digit = digit * digit 
        #     l.append(digit)
        # print(l)
            # if l[-1] in tracker:
            #     return False

        return True 