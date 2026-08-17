class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> subset;
        vector<vector<int>> res;
        dfs(nums,subset,target,0,res);
        return res;
    }
private:
    void dfs(vector<int>& nums,vector<int>& subset,int target, int i, vector<vector<int>>& res) {
        if (target == 0) {
            res.push_back(subset);
            return;
        }
        if (target < 0) {
            return;
        }
        if (i == nums.size()){
            return;
        }
        // TAKE nums[i]
        subset.push_back(nums[i]);
        dfs(nums, subset, target - nums[i], i,res);   // stay at i (reuse allowed)
        subset.pop_back();

        // SKIP nums[i]
        dfs(nums, subset, target, i + 1,res);
    }

};
