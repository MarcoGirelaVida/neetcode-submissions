class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        groups = {}
        nums = set(nums)
        for num in nums:
            ampliable_left = num - 1 in groups and groups[num-1] < num
            ampliable_right = num + 1 in groups and groups[num+1] > num
            if ampliable_left and ampliable_right:
                a = groups[num - 1]     
                b = groups[num + 1]          
                if num - 1 != a:             
                    del groups[num - 1]
                if num + 1 != b:
                    del groups[num + 1]
                groups[a] = b
                groups[b] = a
            elif ampliable_left:
                groups[num] = groups[num - 1]
                groups[groups[num - 1]] = num
                if groups[num - 1] != num:
                    del groups[num - 1]
            elif ampliable_right:
                groups[num] = groups[num + 1]
                groups[groups[num + 1]] = num
                if groups[num + 1] != num:
                    del groups[num + 1]
            else:
                groups[num] = num
        
        max = 0
        for key, value in groups.items():
            if abs(key - value) + 1 > max:
                max = abs(key - value) + 1
        return max
            