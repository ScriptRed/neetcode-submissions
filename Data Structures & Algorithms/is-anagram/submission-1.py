class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters1 = {}
        letters2 = {}

        for letter in s:
            if letter in letters1:
                letters1[letter] += 1
            else:
                letters1[letter] = 1
        
        for letter in t:
            if letter in letters2:
                letters2[letter] += 1
            else:
                letters2[letter] = 1
        
        if len(letters1) != len(letters2):
            return False
        
        return letters2 == letters1