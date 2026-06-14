class Solution:
    def findMin(self, nums: List[int]) -> int:
        """

        """
        # nums.sort()
        l, r = 0, len(nums) - 1 
        low = nums[r]
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            print(l)
            print(r)
            # if nums[mid] >= low:
            if nums[mid] >= low:
                low = min(low, nums[mid])
                l = mid + 1
            # elif mid < low:
            elif nums[mid] < low:
                low = min(low, nums[mid])
                r = mid - 1
        return low 
        # return nums[0]