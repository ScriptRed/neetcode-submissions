class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToIndex = {}
        res = []
        for i in range(len(s)):
            charToIndex[s[i]] = i
        print(charToIndex)
        i = 0
        while i < len(s):
            if i < charToIndex[s[i]]:
                start = i
                reach = charToIndex[s[i]]
                while i < reach:
                    i += 1
                    reach = max(reach,charToIndex[s[i]])
                    print(i,reach)
                res.append(reach + 1 - start)
                i+= 1

            else:
                res.append(1)
                i += 1
        return res       