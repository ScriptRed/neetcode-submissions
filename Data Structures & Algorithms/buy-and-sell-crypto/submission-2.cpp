class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int smallest = prices[0];
        int res = 0;
        for (int x : prices) {
            if (x < smallest) {
                smallest = x;
            };
            int profit = x - smallest;
            res = max(profit,res);
        }
        return res;
    }
};
