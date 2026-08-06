class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0]*len(temperatures)
        for i in range(1,len(temperatures),1):
            if temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    ind = stack.pop()
                    res[ind] = i-ind
                stack.append(i)
        return res


