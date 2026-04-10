class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        this is a sliding window basically 
        we iterate through each number in the array 
        and also have left and right set 
        while left < right 
        we have to see if the total sum = 0 
        if too small then we left += 1
        if too large then we right -=1
        if just right then we add into arr list 

        we also should sort the numbers 
        """
        sort = sorted(nums)
        outcome = []
        for i, n in enumerate(sort):
            if i > 0 and sort[i - 1] == n:
                continue
            left, right = i + 1, len(sort) - 1
            while left < right: 
                t = n + sort[left] + sort[right]
                if t > 0:
                    right -=1

                elif t < 0:
                    left += 1

                else:
                    outcome.append([n, sort[left], sort[right]])
                    right -=1
                    left += 1
                    while left < right and sort[left] == sort[left - 1]:
                        left += 1
        return outcome


