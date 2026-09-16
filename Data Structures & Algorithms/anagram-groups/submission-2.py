class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_set = defaultdict(list)
        for word in strs:
            sorted_word = str(sorted(word))
            anagrams_set[sorted_word].append(word)
        return list(anagrams_set.values())
                