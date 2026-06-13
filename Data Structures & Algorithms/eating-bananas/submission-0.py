class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        
        """
        # l, r, = 0, len(piles) - 1
        # hours = 0
        # for pile in piles:
        #     while l <= r:
        #         mid = (l + r) // 2 
        #         hours += (pile + mid - 1) // mid
        #         print(hours)
        # return 1
        
        l, r = 1, max(piles)  # search over speeds not indexes
        res = max(piles)       # worst case is eating largest pile per hour
        
        while l <= r:
            mid = (l + r) // 2  # candidate speed
            hours = 0
            for pile in piles:  # check if this speed works
                hours += (pile + mid - 1) // mid
            if hours <= h:       # speed works, try slower
                res = mid
                r = mid - 1
            else:                # too slow, go faster
                l = mid + 1
        return res
