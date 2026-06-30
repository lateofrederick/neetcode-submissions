class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        zero_cnt = 0
        output = [0] * len(nums)

        for num in nums:
            if num:
                res *= num
            else:
                zero_cnt += 1

        if zero_cnt > 1:
            return output
        
        for i, c in enumerate(nums):
            if zero_cnt:
                output[i] = 0 if c else res
            else:
                output[i] = res // c
        
        return output
