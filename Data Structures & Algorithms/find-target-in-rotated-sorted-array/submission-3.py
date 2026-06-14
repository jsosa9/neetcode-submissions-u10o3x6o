class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        so we need to find which side of the list that we're on 

        once we find 0 we're on a new side 
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # target in left half
                else:
                    l = mid + 1  # target in right half
            # right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # target in right half
                else:
                    r = mid - 1  # target in left half
        return -1