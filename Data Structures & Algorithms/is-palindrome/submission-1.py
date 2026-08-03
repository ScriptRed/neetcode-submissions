class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = s.lower()
        left = 0
        right = len(s) - 1
        while left < right:
            while not strs[left].isalnum() and left < right:
                left += 1
            while not strs[right].isalnum() and left < right:
                right -= 1
            if strs[left] != strs[right]:
                return False
            left += 1
            right -= 1
        return True