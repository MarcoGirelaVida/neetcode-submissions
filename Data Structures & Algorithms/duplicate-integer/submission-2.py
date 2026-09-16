class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for num in nums:
            if num in unique_elements:
                return True
            unique_elements.add(num)
        return False