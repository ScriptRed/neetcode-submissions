class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s1:
            freq1[ord(c) - ord('a')] += 1
        for c in s2[:len(s1)]:
            freq2[ord(c) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if freq1[i] == freq2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            freq2[idx] += 1
            if freq2[idx] == freq1[idx]:
                matches += 1
            elif freq2[idx] - 1 == freq1[idx]:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            freq2[idx] -= 1
            if freq2[idx] == freq1[idx]:
                matches += 1
            elif freq2[idx] + 1 == freq1[idx]:
                matches -= 1

            l += 1

        return matches == 26