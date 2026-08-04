class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        maxProf = 0
        for i in range(1,len(prices),1):
            if prices[i] > smallest:
                maxProf = max(maxProf,prices[i]-smallest)
            else:
                smallest = prices[i]
        return maxProf