class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = s[0]
        for i in range(n):
            long = s[i]
            l = i-1
            r = i+1
            #odd
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    long = s[l] + long + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            if len(res) < len(long):
                        res = long
                    
        for i in range(n-1):
            if s[i] != s[i+1]:
                continue
            long = s[i] + s[i+1]
            l = i-1
            r = i+2
            #odd
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    long = s[l] + long + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            if len(res) < len(long):
                res = long
        return res



