class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        s2_len = len(s2)

        if r > s2_len:
            return False

        sorted_s1 = "".join(sorted(s1))

        while l < r and r <= s2_len:
            sorted_sub = "".join(sorted(s2[l:r]))

            if sorted_s1 == sorted_sub:
                return True

            l += 1
            r += 1

        return False