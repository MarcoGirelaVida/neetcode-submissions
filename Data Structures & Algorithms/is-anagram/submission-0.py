class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base_dict = dict()
        for char in s:
            if char not in base_dict:
                base_dict[char] = 1
            else:
                base_dict[char] += 1
        
        for char in t:
            if char not in base_dict:
                return False
            else:
                base_dict[char] -= 1
                if base_dict[char] < 0:
                    return False

        for value in base_dict.values():
            if value != 0:
                return False

        return True