class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for index, val in enumerate(nums):
            new_list = []
            for i, val in enumerate(nums):
                if index == i:
                    continue
                else:
                    new_list.append(val)
            total = 1
            for item in new_list:
                total = total * item
            result.append(total)
        return result