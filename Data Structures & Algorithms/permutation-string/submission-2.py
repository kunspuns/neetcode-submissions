class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        freq1 = {}
        freq2 = {}
        for char in s1:
            freq1[char] = freq1.get(char, 0) + 1

        i = 0
        for j, char in enumerate(s2):
            freq2[char] = freq2.get(char, 0) + 1

            # window too big → shrink from left
            if j - i + 1 > len(s1):
                freq2[s2[i]] -= 1
                if freq2[s2[i]] == 0:
                    del freq2[s2[i]]
                i += 1

            # window is exactly right size → check match
            if freq1 == freq2:
                return True

        return False