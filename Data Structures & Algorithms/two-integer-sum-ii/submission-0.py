class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        so for each number we iterate through the array 
        its like 3 pointers 
        one at the end, one at the start, one at current node
        from the current node we get the desired value => taget - current node value 
        then we iterate through the entire array for taht target value 
        once we find it we return the indexes otherwise we dont
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if left < right and numbers[left]+numbers[right] > target:
                right -= 1
            if left < right and numbers[left]+numbers[right] < target:
                left += 1
            if left < right and numbers[left]+numbers[right] == target:
                return list([left + 1, right + 1])



