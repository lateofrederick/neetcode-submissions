class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # {2, 3, 4, 5, 10, 20}
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1

                while (num + length) in numSet:
                    length += 1

                longest = max(length, longest)

        return longest

