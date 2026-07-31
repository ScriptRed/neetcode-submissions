class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            word = "".join(sorted(strs[i]))
            if word in dic:
                dic[word].append(strs[i])
            else:
                dic[word] = [strs[i]]
        return list(dic.values())