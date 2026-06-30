class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        longest_seq = 0

        for n in nums:
            if (n - 1) not in unique_nums:
                length = 0
                while (n + length) in unique_nums:
                    length += 1
                longest_seq = max(length, longest_seq)
        return longest_seq
    
             
