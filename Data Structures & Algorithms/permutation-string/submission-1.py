class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1, freq2 = [0] * 26, [0] * 26
        k = len(s1)

        for i in range(k):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        if freq1 == freq2:
            return True

        for i in range(k, len(s2)):
            left = ord(s2[i - k]) - ord('a')
            freq2[left] -= 1

            right = ord(s2[i]) - ord('a')
            freq2[right] += 1

            if freq1 == freq2:
                return True

        return False