class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        so basically we need ot 
        """
        hashset = set([])
        current_streak, longest = 0, 0
        for n in nums:
            hashset.add(n)
        for n in hashset:
            if n - 1 not in hashset: 
                current_streak = 1
                current = n

                while current + 1 in hashset:
                    current_streak += 1 
                    current += 1 
                if current_streak > longest:
                    longest = current_streak
        return longest

                

            