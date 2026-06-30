class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            length_of_string = len(st)
            s += str(length_of_string) + "#" + st
        
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            sep_index = s.find("#", i)

            str_length = int(s[i:sep_index])

            start = sep_index + 1
            end = start + str_length
            result.append(s[start:end])

            i = end
        return result