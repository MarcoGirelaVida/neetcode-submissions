class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_set = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in anagrams_set:
                anagrams_set[sorted_word] = []
            anagrams_set[sorted_word].append(word)
        return list(anagrams_set.values())
                