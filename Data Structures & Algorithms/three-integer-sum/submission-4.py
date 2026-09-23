class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_ord = sorted(nums)
        nums_map = {val: index for index, val in enumerate(nums_ord)}
        output = set()
        i = 0
        while  i < len(nums_ord) and nums_ord[i] < 1:
            j = len(nums) - 1
            while nums_ord[j] >= 0 and i < j:
                complement = - (nums_ord[i] + nums_ord[j])
                if complement in nums_map and nums_map[complement] != i and nums_map[complement] != j:
                    output.add(tuple(sorted([nums_ord[i], nums_ord[j], complement])))
                j -= 1
            i += 1
        return list(output)