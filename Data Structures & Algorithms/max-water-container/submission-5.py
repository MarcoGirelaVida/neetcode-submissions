class Solution:
    def loss(self, indexA: int, indexB: int, heights: List[int]) -> int:
        return (indexA - indexB) * min(heights[indexA], heights[indexB])

    def maxArea(self, heights: List[int]) -> int:
        r = 0
        l = len(heights) - 1
        max_area = 0
        while r < l:
            max_area = max(self.loss(l, r, heights), max_area)
            heuristic = max(heights[r], heights[l]) * (l - r - 1)
            if heuristic > max_area:
                if heights[r] > heights[l]:
                    l -= 1
                else:
                    r += 1
            else:
                l -= 1
                r += 1
        return max_area
