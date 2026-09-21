class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        groups = {}   # endpoint -> other endpoint of its run
        best = 0
        for num in set(nums):
            lo = groups.pop(num - 1, num)   # left end of the merged run
            hi = groups.pop(num + 1, num)   # right end of the merged run
            groups[lo] = hi
            groups[hi] = lo
            best = max(best, hi - lo + 1)
        return best