class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxFreq = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq[s[right]])

            # shrink window if too many replacements needed
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest