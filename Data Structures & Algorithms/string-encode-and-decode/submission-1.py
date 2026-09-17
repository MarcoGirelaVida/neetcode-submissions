class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        splitter = '\n'
        for word in strs:
            output += word + splitter
        return output

    def decode(self, s: str) -> List[str]:
        splitter = '\n'
        return s.split(splitter)[:-1]