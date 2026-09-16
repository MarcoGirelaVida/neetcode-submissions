class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x : x[1])
        small_half_limit = target // 2
        # Binary search is much better
        split_point = 0
        while sorted_nums[split_point][1] < small_half_limit:
            split_point += 1
        if sorted_nums[split_point][1] == small_half_limit:
            split_point += 1
        small_half = sorted_nums[:split_point]
        big_half = sorted_nums[split_point:]
        for small_num in small_half:
            for big_num in big_half:
                if (small_num[1] + big_num[1]) == target:
                    return sorted([small_num[0], big_num[0]])
                

            


