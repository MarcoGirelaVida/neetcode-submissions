class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small = 0
        big = len(numbers) - 1
        while small < big:
            required = target - numbers[big]
            if required == numbers[small]:
                return [small + 1, big + 1]
            elif required > numbers[small]:
                small += 1
            elif required < numbers[small]:
                big -= 1
                

