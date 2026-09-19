class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_mult_without_zero = 1
        first_zero_location = -1
        output = [0] * len(nums)
        for index, num in enumerate(nums):
            if num != 0:
                total_mult_without_zero *= num
            else:
                if first_zero_location != -1:
                    return output
                first_zero_location = index
        if first_zero_location != -1:
            output[first_zero_location] = total_mult_without_zero
            return output
        
        for i in range(len(nums)):
            output[i] = total_mult_without_zero // nums[i]
        return output