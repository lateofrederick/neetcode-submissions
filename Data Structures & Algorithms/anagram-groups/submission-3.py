class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted in output:
                val = output.get(s_sorted, [])
                val.append(s)
            else:
                output[s_sorted] = [s]

        return list(output.values())  
            