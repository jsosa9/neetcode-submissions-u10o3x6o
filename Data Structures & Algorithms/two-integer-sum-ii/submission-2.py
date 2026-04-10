class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right: 
            # if current sum is greater then target right -= 1 
            # if current sum is smaller then the target left -= 1
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right-=1
            elif current_sum < target:
                left+=1
            else:
                return [left + 1, right + 1]