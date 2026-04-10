class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        this is a sliding window approach 
        we take the left pointer at 0
        right pointer at the end 
        if the sum of them are too large we -= 1 on right 
        if the sum is too small we += 1 on left 
        and if the sum is our solution then we add it into the arr

        we need to watch out for dup
        """
        left, right = 0, len(numbers) - 1
        output = []
        while left < right:
            if left < right and numbers[left] + numbers[right] > target:
                right-= 1
            if left < right and numbers[left] + numbers[right] < target:
                left += 1
            if left < right and numbers[left] + numbers[right] == target:
                return list([left+1, right+1])
