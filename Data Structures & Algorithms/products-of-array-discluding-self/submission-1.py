class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
    
        initial_index = 0
        current_index = 0
        
        while current_index < len(nums):
            temp = []
            if current_index == initial_index:
                temp = nums[initial_index+1:]
            elif current_index == len(nums) - 1 :
                temp = nums[:-1]
            else:
                
                temp = nums[initial_index:current_index] + nums[current_index+1:]
            
            total = 1
            print(temp)
            for item in temp:
                total = total * item
            result.append(total)
            current_index += 1
        return result