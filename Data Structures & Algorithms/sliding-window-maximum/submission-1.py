class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        n = len(nums)
        output = []

        while r <= n:
            maxV = float('-inf')
            
            for i in nums[l:r]:
                maxV = max(maxV, i)
            
            output.append(int(maxV))
            l += 1
            r += 1
        
        return output