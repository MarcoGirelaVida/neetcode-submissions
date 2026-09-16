class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        for letter in s:
            s_dict[letter] = 1 if letter not in s_dict else s_dict[letter] + 1

        for letter in t:
            if letter not in s_dict or s_dict[letter] == 0:
                return False
            s_dict[letter] -= 1

        for value in s_dict.values():
            if value != 0:
                return False

        return True
