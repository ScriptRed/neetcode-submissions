class Solution:
    def trap(self, height: List[int]) -> int:
        tot = 0
        left = 0
        right = len(height) - 1
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        for i in range(1, len(height), 1):
            prefix[i] = max(height[i-1],prefix[i-1])
        for i in range(len(height)-2, -1, -1):
            print(i)
            suffix[i] = max(height[i+1],suffix[i+1])
        print(prefix,suffix)
        for i in range(len(height)):
            tot += max(min(prefix[i], suffix[i]) - height[i],0)

        return tot
            
        