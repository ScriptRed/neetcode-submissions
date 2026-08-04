class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        found = {}
        i = 0
        start = 0
        while i < len(s):
            if s[i] in found and found[s[i]] >= start:
                longest = max(longest,i - start)
                start = found[s[i]] + 1
                found[s[i]] = i
                i += 1
            else:
                found[s[i]] = i
                i += 1
        return max(i - start,longest)
            



        