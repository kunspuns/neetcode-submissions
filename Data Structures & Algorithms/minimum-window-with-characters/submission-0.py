class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t): return ""

        freqt = {}
        for char in t:
            freqt[char] = freqt.get(char, 0) + 1

        freqs = {}
        matches = 0
        target = len(freqt)
        i = 0
        min_len = float('inf')
        min_start = 0

        for j, char in enumerate(s):
            # 1. add char to freqs
            freqs[char] = freqs.get(char,0) + 1
            # 2. if freqs[char] == freqt[char], increment matches
            if freqs[char] == freqt.get(char,0): matches += 1
            # 3. while matches == target (window is valid):
            while matches == target:
            #        update min_len and min_start if current window is smaller
                if j-i+1<min_len:
                    min_len = j-i+1
                    min_start=i
            #        shrink from left: decrement freqs[s[i]]
                
                freqs[s[i]] -= 1
            #        if freqs[s[i]] < freqt[s[i]], decrement matches
                if freqs[s[i]]<freqt.get(s[i],0): matches -= 1
            #        i += 1
                i += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]