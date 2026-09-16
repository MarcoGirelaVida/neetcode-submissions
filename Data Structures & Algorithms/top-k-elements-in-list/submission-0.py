class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counts = {}
        top_k = []
        for num in nums:
            nums_counts[num] = nums_counts.get(num, 0) + 1
        inverted_num_counts = ((value, key) for key, value in nums_counts.items())
        for entry in inverted_num_counts:
            if len(top_k) < k or entry[0] > top_k[0][0]:
                if len(top_k) == k:
                    heapq.heappop(top_k)
                heapq.heappush(top_k, entry)
        return [pair[1] for pair in top_k]

