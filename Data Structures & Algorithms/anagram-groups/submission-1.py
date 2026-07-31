class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in dic:
                dic[tuple(count)] = [word]
            else:
                dic[tuple(count)].append(word)
        return list(dic.values())