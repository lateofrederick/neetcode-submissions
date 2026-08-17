class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vals = set()

        for i in nums:
            if i in vals:
                return i
            
            vals.add(i)
                  
        return -1