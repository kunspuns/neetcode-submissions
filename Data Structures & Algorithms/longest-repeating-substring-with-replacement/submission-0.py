class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}        # char → count in current window
        i = 0
        max_freq = 0     # highest frequency of any single char in window
        result = 0

        for j, char in enumerate(s):
            # 1. add char to freq map
            freq[char] = freq.get(char,0) + 1
            # 2. update max_freq
            max_freq = max(max_freq,freq[char])
            # 3. if window is invalid (replacements needed > k), shrink from left
            if (j-i+1) - max_freq>k: 
                freq[s[i]] -= 1 
                i += 1
            # 4. update result with current window size
            result=max(result,j-i+1)

        return result
        