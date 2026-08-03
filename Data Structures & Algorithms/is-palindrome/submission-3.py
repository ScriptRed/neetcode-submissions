class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ''.join(ch.lower() for ch in s if ch.isalnum())
        left = 0
        right = len(strs) - 1
        while left < right:
            if strs[left] != strs[right]:
                return False
            left += 1
            right -= 1
        return True