class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}

        for val in s:
            dict_1[val] = dict_1.get(val, 0) + 1

        for val in t:
            dict_2[val] = dict_2.get(val, 0) + 1
        
        return dict_1 == dict_2