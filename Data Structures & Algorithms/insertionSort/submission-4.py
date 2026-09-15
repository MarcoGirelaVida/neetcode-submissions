# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
from collections import deque
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = [pairs]
        ordered_pairs = pairs.copy()

        for i in range(len(ordered_pairs) - 1):
            prior = i
            post = i+1
            if ordered_pairs[prior].key > ordered_pairs[post].key: 
                while prior > 0 and ordered_pairs[prior-1].key > ordered_pairs[post].key: 
                    prior -= 1
                ordered_pairs.insert(prior, ordered_pairs[post])
                ordered_pairs.pop(post+1)
            output.append(ordered_pairs.copy())
        if (output == [[]]):
            return []
        return output

