class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total < target:
                print(1)
                left+=1 
            elif total > target:
                print(2)
                right-=1
            else:
                print(total)
                print(target)
                return [left + 1, right + 1]
        return [left,right]