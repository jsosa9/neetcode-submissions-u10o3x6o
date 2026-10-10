class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 numbers must add up to the target 
        index1 < index 2 both cant be equal 
        and you cant use the same element twice
        """ 
        l = 0 
        r = len(numbers) - 1

        while l < r:
            x = numbers[l] + numbers[r]
            if x > target:
                r-=1
            elif x < target:
                l +=1 
            else:
                return [l + 1, r + 1]
        return [0,0]