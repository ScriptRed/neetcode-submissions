class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        found = {}
        i = 0
        start = 0
        while i < len(s):
            if s[i] in found and found[s[i]] >= start:
                longest = max(longest,curr)
                curr = i - found[s[i]]
                start = found[s[i]] + 1
                found[s[i]] = i
                i += 1

            else:
                found[s[i]] = i
                i += 1
                curr += 1
        return max(curr,longest)
            



        