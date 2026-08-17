class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        n = k 
        m_len = 0
        while r < len(nums): 
            if nums[r] == 0:
                n -= 1 
            if n < 0:
                if nums[l] == 0:
                    n += 1
                l+=1 
            m_len = max(m_len, r - l + 1)
            r+=1 
        return m_len