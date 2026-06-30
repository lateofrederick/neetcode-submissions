class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        val_a = {}
        val_b = {}

        s_length, t_length = len(s), len(t)

        if s_length != t_length:
            return False

        i = 0
        while i < s_length:
            val_a[s[i]] = val_a.get(s[i], 0) + 1
            val_b[t[i]] = val_b.get(t[i], 0) + 1
            i += 1

        return val_a == val_b
