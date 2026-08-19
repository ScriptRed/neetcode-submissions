class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        if (n == 0) {
            return 0;
        }
        vector<int> arrFirst(n - 1);
        vector<int> arrSecond(n - 1);
        int rob1 = 0;int rob2 = 0;

        for (int i = 0;i < n - 1; i++) {
            int temp = max(nums[i] + rob1,rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        int incFirst = max(rob1,rob2);
        rob1 = 0;rob2 = 0;
        for (int i = 1;i < n; i++) {
            int temp = max(nums[i] + rob1,rob2);
            rob1 = rob2;
            rob2 = temp;
        }
        return max(max(rob1,rob2),incFirst);
        
    }
};
