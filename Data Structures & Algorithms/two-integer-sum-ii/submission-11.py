class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        only one valid soltuon 
        """
        s, e = 0, len(numbers) - 1

        while s < e:
            k = numbers[s] + numbers[e]
            if k == target:
                return [s + 1, e + 1]
            elif k < target:
                s += 1
            else:
                e -= 1