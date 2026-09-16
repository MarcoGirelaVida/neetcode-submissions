class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = {}
        top_k = []
        for num in nums:
            nums_counts[num] = nums_counts.get(num, 0) + 1
        for num, freq in nums_counts.items():
            if len(top_k) < k or freq > top_k[0][0]:
                if len(top_k) == k:
                    heapq.heappop(top_k)
                heapq.heappush(top_k, (freq, num))
        return [pair[1] for pair in top_k]

