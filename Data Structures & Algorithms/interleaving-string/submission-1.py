class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        stateMap = {}
        def dfs(s1index, s2index):
            if (s1index, s2index) in stateMap:
                return stateMap[(s1index, s2index)]

            if s1index == len(s1):
                result = s2[s2index:] == s3[s1index + s2index:]
            elif s2index == len(s2):
                result = s1[s1index:] == s3[s1index + s2index:]
            else:
                c = s3[s1index + s2index]
                result = False
                if c == s1[s1index]:
                    result = result or dfs(s1index + 1, s2index)
                if c == s2[s2index]:
                    result = result or dfs(s1index, s2index + 1)

            stateMap[(s1index, s2index)] = result
            return result

        
        return dfs(0,0)