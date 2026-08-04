class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        found = {}
        start = 0
        for i in range(len(s)):
            if s[i] in found and found[s[i]] >= start:
                longest = max(longest,i - start)
                start = found[s[i]] + 1
            found[s[i]] = i
            longest = max(longest,i - start + 1)
        return longest
            



        